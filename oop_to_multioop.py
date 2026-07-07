#!/usr/bin/env python3
"""Translate Python OOP benchmark artifacts into MultiOOP JSONL files.

The source data in ``data/oop-python.jsonl`` contains natural-language tasks,
Python ``assert candidate(...) == expected`` tests, and Python structural
matching tokens.  This script converts those benchmark artifacts to the target
MultiOOP languages while preserving task ids and the original OOP
calling convention encoded in each ``test_function``.

If a record also contains a Python reference implementation in ``code``,
``solution``, ``reference``, ``reference_code``, or ``canonical_solution``, the
script additionally invokes the AST -> IR -> template renderer from
``oop_to_multioop_converter.py`` and writes the translated implementation back
to the target-language ``code`` field.
"""

from __future__ import annotations

import argparse
import ast
import copy
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Literal


Language = Literal["cpp", "java", "cs", "php", "js", "ruby", "swift"]

LANGUAGE_NAMES: dict[Language, str] = {
    "cpp": "C++",
    "java": "Java",
    "cs": "C#",
    "php": "PHP",
    "js": "JavaScript",
    "ruby": "Ruby",
    "swift": "Swift",
}

DEFAULT_LANGUAGES: tuple[Language, ...] = ("cpp", "java", "cs", "php", "js", "ruby", "swift")
CODE_TARGETS: dict[Language, str] = {
    "cpp": "cpp",
    "java": "java",
    "cs": "csharp",
    "php": "php",
    "js": "javascript",
}
SOURCE_CODE_FIELDS: tuple[str, ...] = (
    "code",
    "solution",
    "reference",
    "reference_code",
    "canonical_solution",
)


@dataclass(frozen=True)
class CandidateCall:
    class_name: str
    constructor_params: tuple[str, ...]
    method_name: str
    method_params: tuple[str, ...]


@dataclass(frozen=True)
class TestCase:
    args: tuple[Any, ...]
    expected: Any


@dataclass(frozen=True)
class CodeConversion:
    kept: bool
    code: str = ""
    issues: tuple[str, ...] = ()


class AstIrCodeConverter:
    """Adapter around the benchmark AST/IR converter used for source code."""

    def has_source_code(self, record: dict[str, Any]) -> bool:
        return find_source_code(record) is not None

    def convert(self, record: dict[str, Any], language: Language) -> CodeConversion:
        source = find_source_code(record)
        if source is None:
            return CodeConversion(kept=False, issues=("missing Python reference code",))

        target = CODE_TARGETS.get(language)
        if target is None:
            name = LANGUAGE_NAMES[language]
            return CodeConversion(kept=False, issues=(f"AST/IR code conversion is not implemented for {name}",))

        try:
            from oop_to_multioop_converter import convert_sample
        except ImportError as exc:
            return CodeConversion(kept=False, issues=(f"cannot import AST/IR converter: {exc}",))

        converter_sample = build_code_converter_sample(record, source)
        result = convert_sample(converter_sample, [target])
        if not result.get("kept"):
            return CodeConversion(kept=False, issues=tuple(result.get("issues", ())))

        outputs = result.get("outputs", {})
        payload = outputs.get(target, {})
        code = str(payload.get("code", ""))
        if not code.strip():
            return CodeConversion(kept=False, issues=("AST/IR converter produced empty code",))
        return CodeConversion(kept=True, code=code)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(records: Iterable[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def find_source_code(record: dict[str, Any]) -> str | None:
    for field_name in SOURCE_CODE_FIELDS:
        value = record.get(field_name)
        if isinstance(value, str) and value.strip():
            return value
    return None


def build_code_converter_sample(record: dict[str, Any], source: str) -> dict[str, Any]:
    sample = {
        "task_id": record.get("task_id") or record.get("sample_id") or record.get("id") or "sample",
        "prompt": record.get("prompt")
        or record.get("instruction")
        or record.get("requirement")
        or record.get("question")
        or "",
        "code": source,
    }

    tests = record.get("tests") or record.get("test") or record.get("test_code")
    if isinstance(tests, str) and tests.strip():
        sample["tests"] = tests
    return sample


def translate_record(
    record: dict[str, Any],
    language: Language,
    code_converter: AstIrCodeConverter | None = None,
    strict_code: bool = False,
) -> dict[str, Any]:
    translated = copy.deepcopy(record)
    translated["question"] = rewrite_question(str(record.get("question", "")), language)

    test_function = str(record["test_function"])
    match_function = record.get("test_match_function", [])
    try:
        parsed_call = parse_candidate_call(test_function)
    except (SyntaxError, ValueError) as exc:
        parsed_call = fallback_candidate_call(test_function, match_function)
        if parsed_call is None:
            task_id = record.get("task_id", "<unknown>")
            raise ValueError(f"{task_id}: {exc}") from exc
    call = reconcile_candidate_call(parsed_call, match_function)
    test_cases = [parse_assertion(item) for item in record.get("test_list", [])]
    translated["test_list"] = render_tests(test_cases, call, language)

    translated["test_match_function"] = translate_match_function(
        record.get("test_match_function", []),
        language,
    )
    translated["test_matching"] = build_test_matching(translated["test_match_function"])

    if code_converter is not None and code_converter.has_source_code(record):
        code_result = code_converter.convert(record, language)
        if code_result.kept:
            translated["code"] = code_result.code
            translated["source_language"] = "Python"
            translated["target_language"] = LANGUAGE_NAMES[language]
        elif strict_code:
            task_id = record.get("task_id", "<unknown>")
            issues = "; ".join(code_result.issues)
            raise ValueError(f"{task_id}: AST/IR code conversion failed: {issues}")
        else:
            translated["code_translation_issues"] = list(code_result.issues)

    return translated


def rewrite_question(question: str, language: Language) -> str:
    target = LANGUAGE_NAMES[language]
    rewritten = re.sub(r"\bPython\s+language\b", f"{target} language", question, flags=re.IGNORECASE)
    rewritten = re.sub(r"\busing\s+Python\b", f"using {target}", rewritten, flags=re.IGNORECASE)
    rewritten = re.sub(r"\bin\s+Python\b", f"in {target}", rewritten, flags=re.IGNORECASE)
    rewritten = re.sub(r"\bPython\b", target, rewritten, flags=re.IGNORECASE)

    if language in {"cpp", "java", "cs", "swift"}:
        rewritten = re.sub(
            r"\binstance attribute called\b",
            "instance private attribute called",
            rewritten,
            flags=re.IGNORECASE,
        )
        rewritten = re.sub(r"\badd two attributes\b", "add two private attributes", rewritten, flags=re.IGNORECASE)
        rewritten = re.sub(r"\bwith the \*\*(.*?)\*\* attribute\b", r"with the **\1** private attribute", rewritten)

    return rewritten


def parse_candidate_call(test_function: str) -> CandidateCall:
    tree = ast.parse(test_function)
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    if not functions:
        raise ValueError("test_function must define candidate")

    returns = [node for node in ast.walk(functions[0]) if isinstance(node, ast.Return)]
    if not returns or returns[0].value is None:
        raise ValueError("candidate must return a class method call")

    method_call = returns[0].value
    if isinstance(method_call, ast.Compare) and isinstance(method_call.left, ast.Attribute):
        # A few source rows contain malformed wrappers such as
        # ``return SN_X(...).method==5()``.  The benchmark tests still encode the
        # actual inputs and expected outputs, so recover the intended OOP call.
        instance_call = method_call.left.value
        if isinstance(instance_call, ast.Call) and isinstance(instance_call.func, ast.Name):
            return CandidateCall(
                class_name=instance_call.func.id,
                constructor_params=tuple(name_of(arg) for arg in instance_call.args),
                method_name=method_call.left.attr,
                method_params=(),
            )
    if not isinstance(method_call, ast.Call) or not isinstance(method_call.func, ast.Attribute):
        raise ValueError("candidate return value must be an instance method call")

    instance_call = method_call.func.value
    if not isinstance(instance_call, ast.Call) or not isinstance(instance_call.func, ast.Name):
        raise ValueError("candidate must instantiate a class before calling the method")

    return CandidateCall(
        class_name=instance_call.func.id,
        constructor_params=tuple(name_of(arg) for arg in instance_call.args),
        method_name=method_call.func.attr,
        method_params=tuple(name_of(arg) for arg in method_call.args),
    )


def reconcile_candidate_call(call: CandidateCall, match_function: Any) -> CandidateCall:
    """Use structural-match tokens to repair obvious source metadata typos."""
    class_name = call.class_name
    method_name = call.method_name

    if isinstance(match_function, list):
        for pattern in match_function:
            if not isinstance(pattern, list):
                continue
            classes = []
            methods = []
            for token in pattern:
                if not isinstance(token, str):
                    continue
                class_match = re.fullmatch(r"class\s+([A-Za-z_][A-Za-z0-9_]*)", token)
                method_match = re.fullmatch(r"def\s+([A-Za-z_][A-Za-z0-9_]*)", token)
                if class_match:
                    classes.append(class_match.group(1))
                if method_match:
                    methods.append(method_match.group(1))
            if classes and call.class_name not in classes:
                class_name = classes[0]
            if methods and call.method_name not in methods:
                public_methods = [name for name in methods if not name.startswith("_")]
                method_name = public_methods[-1] if public_methods else methods[-1].lstrip("_")
            break

    return CandidateCall(
        class_name=class_name,
        constructor_params=call.constructor_params,
        method_name=method_name,
        method_params=call.method_params,
    )


def fallback_candidate_call(test_function: str, match_function: Any) -> CandidateCall | None:
    classes, methods = extract_match_hints(match_function)
    if not classes or not methods:
        return None

    signature_match = re.search(r"def\s+candidate\(([^)]*)\)", test_function)
    all_params = split_params(signature_match.group(1)) if signature_match else []

    constructor_params = all_params
    constructor_match = re.search(r"return\s+([A-Za-z_][A-Za-z0-9_]*)\(([^)]*)\)\.", test_function)
    class_name = classes[0]
    if constructor_match:
        class_name = constructor_match.group(1)
        constructor_params = split_params(constructor_match.group(2))

    return CandidateCall(
        class_name=class_name,
        constructor_params=tuple(constructor_params),
        method_name=methods[-1],
        method_params=(),
    )


def extract_match_hints(match_function: Any) -> tuple[list[str], list[str]]:
    if not isinstance(match_function, list):
        return [], []
    for pattern in match_function:
        if not isinstance(pattern, list):
            continue
        classes: list[str] = []
        methods: list[str] = []
        for token in pattern:
            if not isinstance(token, str):
                continue
            class_match = re.fullmatch(r"class\s+([A-Za-z_][A-Za-z0-9_]*)", token)
            method_match = re.fullmatch(r"def\s+([A-Za-z_][A-Za-z0-9_]*)", token)
            if class_match:
                classes.append(class_match.group(1))
            if method_match:
                methods.append(method_match.group(1).lstrip("_"))
        return classes, methods
    return [], []


def split_params(params: str) -> list[str]:
    return [param.strip() for param in params.split(",") if param.strip()]


def parse_assertion(assertion: str) -> TestCase:
    tree = ast.parse(assertion)
    if len(tree.body) != 1 or not isinstance(tree.body[0], ast.Assert):
        raise ValueError(f"unsupported test statement: {assertion}")

    expr = tree.body[0].test
    if not isinstance(expr, ast.Compare) or len(expr.ops) != 1 or not isinstance(expr.ops[0], ast.Eq):
        raise ValueError(f"test must be an equality assertion: {assertion}")
    if len(expr.comparators) != 1:
        raise ValueError(f"test must compare candidate(...) with one expected value: {assertion}")

    call = expr.left
    if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name) or call.func.id != "candidate":
        raise ValueError(f"left side must be candidate(...): {assertion}")

    return TestCase(
        args=tuple(ast.literal_eval(arg) for arg in call.args),
        expected=ast.literal_eval(expr.comparators[0]),
    )


def name_of(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    raise ValueError(f"expected a simple parameter name, got {node.__class__.__name__}")


def render_tests(test_cases: list[TestCase], call: CandidateCall, language: Language) -> list[str]:
    lines: list[str] = []
    if language == "js":
        lines.append('const assert = require("node:assert/strict");')

    for index, test_case in enumerate(test_cases):
        env = {f"content{i + 1}": value for i, value in enumerate(test_case.args)}
        invocation = render_invocation(call, env, language)
        expected = literal(test_case.expected, language)

        if language == "cpp":
            lines.append(f"assert({invocation} == {expected});")
        elif language == "java":
            if isinstance(test_case.expected, (str, list)):
                lines.append(f"assert {invocation}.equals({expected});")
            else:
                lines.append(f"assert {invocation} == {expected};")
        elif language == "cs":
            lines.append(f"Debug.Assert({invocation} == {expected});")
        elif language == "php":
            lines.append(
                f'if ({invocation} !== {expected}) {{ throw new Exception("Test {index + 1} failed"); }}'
            )
        elif language == "js":
            lines.append(f"assert.deepStrictEqual({invocation}, {expected});")
        elif language == "ruby":
            lines.append(f'raise "Test {index + 1} failed" unless {invocation} == {expected}')
        elif language == "swift":
            lines.append(f"assert({invocation} == {expected})")
        else:
            raise ValueError(f"unsupported language: {language}")

    return lines


def render_invocation(call: CandidateCall, env: dict[str, Any], language: Language) -> str:
    constructor_args = ", ".join(literal(env[name], language) for name in call.constructor_params if name in env)
    method_args = ", ".join(literal(env[name], language) for name in call.method_params if name in env)

    if language == "cpp":
        instance = f"{call.class_name}({constructor_args})"
        return f"{instance}.{call.method_name}({method_args})"
    if language == "java":
        return f"new {call.class_name}({constructor_args}).{call.method_name}({method_args})"
    if language == "cs":
        return f"new {call.class_name}({constructor_args}).{call.method_name}({method_args})"
    if language == "php":
        return f"(new {call.class_name}({constructor_args}))->{call.method_name}({method_args})"
    if language == "js":
        return f"new {call.class_name}({constructor_args}).{call.method_name}({method_args})"
    if language == "ruby":
        return f"{call.class_name}.new({constructor_args}).{call.method_name}({method_args})"
    if language == "swift":
        return f"{call.class_name}({constructor_args}).{call.method_name}({method_args})"
    raise ValueError(f"unsupported language: {language}")


def literal(value: Any, language: Language) -> str:
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        if language == "cpp":
            return "nullptr"
        if language == "ruby":
            return "nil"
        return "nil" if language == "swift" else "null"
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, list):
        inner = ", ".join(literal(item, language) for item in value)
        if language == "cpp":
            return f"std::vector<{cpp_vector_type(value)}>{{{inner}}}"
        if language == "java":
            return f"Arrays.asList({inner})"
        if language == "cs":
            return f"new List<{cs_list_type(value)}>{{{inner}}}"
        return f"[{inner}]"
    raise ValueError(f"unsupported literal value: {value!r}")


def cpp_vector_type(values: list[Any]) -> str:
    if not values:
        return "int"
    first = values[0]
    if isinstance(first, bool):
        return "bool"
    if isinstance(first, int):
        return "int"
    if isinstance(first, float):
        return "double"
    if isinstance(first, str):
        return "std::string"
    if isinstance(first, list):
        return f"std::vector<{cpp_vector_type(first)}>"
    return "auto"


def cs_list_type(values: list[Any]) -> str:
    if not values:
        return "object"
    first = values[0]
    if isinstance(first, bool):
        return "bool"
    if isinstance(first, int):
        return "int"
    if isinstance(first, float):
        return "double"
    if isinstance(first, str):
        return "string"
    if isinstance(first, list):
        return f"List<{cs_list_type(first)}>"
    return "object"


def translate_match_function(match_function: Any, language: Language) -> list[list[str]]:
    if not isinstance(match_function, list):
        return []
    return [translate_match_pattern(pattern, language) for pattern in match_function if isinstance(pattern, list)]


def translate_match_pattern(pattern: list[Any], language: Language) -> list[str]:
    translated: list[str] = []
    for token in pattern:
        if not isinstance(token, str):
            continue
        translated.extend(translate_match_token(token, language))
    return dedupe(translated)


def translate_match_token(token: str, language: Language) -> list[str]:
    class_match = re.fullmatch(r"class\s+([A-Za-z_][A-Za-z0-9_]*)", token)
    if class_match:
        name = class_match.group(1)
        return [f"public class {name}"] if language in {"java", "cs"} else [f"class {name}"]

    def_match = re.fullmatch(r"def\s+([A-Za-z_][A-Za-z0-9_]*)", token)
    if def_match:
        name = def_match.group(1)
        private = name.startswith("__") or name.startswith("_private")
        clean_name = name[2:] if name.startswith("__") else name.lstrip("_")
        if language == "php":
            access = "private" if private else "public"
            return [f"{access} function {clean_name}"]
        if language == "js":
            return [f"#{clean_name}" if private else clean_name]
        if language == "ruby":
            return ["private", f"def {clean_name}"] if private else [f"def {clean_name}"]
        if language == "swift":
            access = "private " if private else ""
            return [f"{access}func {clean_name}"]
        if private:
            return ["private", clean_name]
        return [clean_name]

    if token == "super().__init__(nums)":
        if language == "cpp":
            return [": FDSB(nums)"]
        if language == "java":
            return ["super(nums);"]
        if language == "cs":
            return [": base(nums)"]
        if language == "php":
            return ["parent::__construct($nums);"]
        if language == "js":
            return ["super(nums);"]
        if language == "ruby":
            return ["super(nums)"]
        if language == "swift":
            return ["super.init(nums)"]

    return [token]


def build_test_matching(match_function: list[list[str]]) -> str:
    return f"assert candidate({json.dumps(match_function, ensure_ascii=False)}) == True"


def dedupe(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def parse_languages(values: list[str]) -> list[Language]:
    normalized: list[Language] = []
    aliases = {"c++": "cpp", "c#": "cs", "javascript": "js", "rb": "ruby"}
    for value in values:
        language = aliases.get(value.lower(), value.lower())
        if language not in LANGUAGE_NAMES:
            raise ValueError(f"unsupported language: {value}")
        normalized.append(language)  # type: ignore[arg-type]
    return normalized


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Python OOP JSONL into MultiOOP JSONL files.")
    parser.add_argument("--input", type=Path, default=Path("data/oop-python.jsonl"))
    parser.add_argument("--output-dir", type=Path, default=Path("data/generated"))
    parser.add_argument("--languages", nargs="+", default=list(DEFAULT_LANGUAGES))
    parser.add_argument(
        "--no-code",
        action="store_true",
        help="Only translate requirement descriptions, tests, and matchers; skip AST/IR code conversion.",
    )
    parser.add_argument(
        "--strict-code",
        action="store_true",
        help="Fail if a record with Python source code cannot be converted through the AST/IR pipeline.",
    )
    args = parser.parse_args()

    records = read_jsonl(args.input)
    languages = parse_languages(args.languages)
    code_converter = None if args.no_code else AstIrCodeConverter()
    for language in languages:
        translated = [
            translate_record(
                record,
                language,
                code_converter=code_converter,
                strict_code=args.strict_code,
            )
            for record in records
        ]
        output_path = args.output_dir / f"oop-{language}.jsonl"
        write_jsonl(translated, output_path)
        print(f"{LANGUAGE_NAMES[language]}: wrote {len(translated)} records to {output_path}")


if __name__ == "__main__":
    main()
