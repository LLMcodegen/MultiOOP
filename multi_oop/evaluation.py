import os
import sys
import fire
import json
import gzip
import regex
import numpy as np
import itertools
import ast

from typing import *
from tqdm.auto import tqdm
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from .data import stream_jsonl
from .execution import check_correctness
IMPORT_HELPER = {
    "python": [
        "import math",
        "import re",
        "import sys",
        "import copy",
        "import datetime",
        "import itertools",
        "import collections",
        "import heapq",
        "import functools",
        "import hashlib",
        "import numpy",
        "import numpy as np",
        "import string",
        "from typing import *",
        "from collections import *",
    ],
    "go"    : [
        "math",
        "strings",
        "fmt",
        "strconv",
        "time",
        "bytes",
        "regexp",
        "sort",
        "math/rand",
        "crypto/md5",
    ],
    "cpp"   : [
        "#include<stdlib.h>",
        "#include<algorithm>",
        "#include<math.h>",
        "#include<stdio.h>",
        "#include<vector>",
        "#include<string>",
        "#include<climits>",
        "#include<cstring>",
        "#include<iostream>",
        "#include<cassert>",
        "#include<unordered_map>"
    ],
    "cs": ["using System.Numerics;", "using System.Diagnostics;", "using System.Collections.Generic;", "using System.Linq;", "using System.Text;", "using System.Security.Cryptography;", "using System.Collections.Generic;"],
    "java": ["import java.util.*;", 
             "import java.lang.reflect.*;", 
             "import java.security.*;", 
             "import java.math.*;", 
             "import java.io.*;", 
             "import java.util.stream.*;"
             ]
}
# "import org.javatuples.*;", 

LANGUAGE_NAME = {
    "cpp"   : "CPP",
    "go"    : "Go",
    "java"  : "Java",
    "js"    : "JavaScript",
    "python": "Python",
}


def read_dataset(
    data_file: str = None,
    dataset_type: str = "humaneval",
    num_shot=None,
) -> Dict:
    """
    Reads a dataset and returns a dictionary of tasks.
    """
    if num_shot is not None:
        print(f"{num_shot}-shot setting...")
    
    if "data" in dataset_type.lower():
        if data_file is None:
            current_path = os.path.dirname(os.path.abspath(__file__))
            data_file = os.path.join(current_path, "..", "humaneval-x", "python", "data", "humaneval_python.jsonl.gz")
        dataset = {task["task_id"]: task for task in stream_jsonl(data_file)}
    else:
        raise f"Dataset: {dataset_type} not supported."

    return dataset

def estimate_pass_at_k(
        num_samples: Union[int, List[int], np.ndarray],
        num_correct: Union[List[int], np.ndarray],
        k: int
) -> np.ndarray:
    """
    Estimates pass@k of each problem and returns them in an array.
    """

    def estimator(n: int, c: int, k: int) -> float:
        """
        Calculates 1 - comb(n - c, k) / comb(n, k).
        """
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    if isinstance(num_samples, int):
        num_samples_it = itertools.repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return np.array([estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)])

def process_humaneval_test(sample, problems, example_test=False, is_mbpp=False, language="python", metric="passk"):
    """
    Processes a sample for evaluation.
    """
    task_id = sample["task_id"]
    # print('-----------------------')
    # print(task_id)
    if is_mbpp:
        return sample["generation"] + "\n" + "\n".join(problems[task_id]["test"])

    prompt = sample["prompt"]
    code = sample["generation"]
    entry_point = problems[task_id]["entry_point"]
    if example_test and "example_test" in problems[task_id] and problems[task_id]["example_test"] != "":
        test = problems[task_id]["example_test"]
    else:
        if language == "python":
            test_exam = f"def check({entry_point}):"
            test = problems[task_id]["test_list"]
            # test_len = len(test)
            # if test_len >= 15:
            #     test = test[:15]
            test_func = problems[task_id]["test_function"]
            for test_idx in test:
                test_exam = test_exam + "\n    " + test_idx
        elif language == "java":
            test = problems[task_id]["test_list"]
            # test_len = len(test)
            # if test_len >= 30:
            #     test = test[:30]
            if metric == "passo":
                test_match_func = problems[task_id]["test_match_function"]
                test_match_func = test_match_func[0]
                my_string = ', '.join(f'"{item.replace("public ", "")}"' for item in test_match_func)

                # my_string = ', '.join(f'"{item}"' for item in test_match_func)
                converted_code = f"{code}"
                
                test_exam = "public class Problem {\n    public static void main(String[] args) {\n"
                test_match = f"\n        List<String> input_match = Arrays.asList({my_string});\n        String code = \"{repr(converted_code)}\";\n        boolean allMatches = input_match.stream().allMatch(code::contains);\n        assert(allMatches);\n"
                test_exam = test_exam + test_match
                for test_idx in test:
                    test_exam = test_exam + "\n        " + test_idx + ";"
                test_exam = test_exam + "\n    }\n}" 
                # print(test_exam)
            elif metric == "passk":
                test_exam = "public class Problem {\n    public static void main(String[] args) {\n"
                for test_idx in test:
                    test_exam = test_exam + "\n        " + test_idx + ";"
                test_exam = test_exam + "\n    }\n}" 
        elif language == "cpp":
            test = problems[task_id]["test_list"]
            # test_len = len(test)
            # if test_len >= 30:
            #     test = test[:30]
            if metric == "passo":
                test_exam = "int main() {\n"
                test_match_func = problems[task_id]["test_match_function"]
                test_match_func = test_match_func[0]
                my_string = ', '.join(f'"{item}"' for item in test_match_func)
                converted_code = f"{code}"
                
                match_content = "\nbool allStringsInTarget(const std::vector<std::string>& my_list, const std::string& target_string) {\n    for (const auto& item : my_list) {\n        if (target_string.find(item) == std::string::npos) {\n            return false;\n        }\n    }\n    return true;\n}\n"
                test_exam = match_content + test_exam
                test_exam = test_exam + "\n    std::vector<std::string> my_list = {" + f"{my_string}" + "};\n    std::string target_string = " + f"\"{repr(converted_code)}\";\n    assert(allStringsInTarget(my_list, target_string) == true);\n"
                for test_idx in test:
                    test_exam = test_exam + "\n    " + test_idx +";"
                test_exam = test_exam + "\n    return 0;\n}"
            elif metric == "passk":
                test_exam = "int main() {\n"
                for test_idx in test:
                    test_exam = test_exam + "\n    " + test_idx +";"
                test_exam = test_exam + "\n    return 0;\n}"
        elif language == "cs":
            test = problems[task_id]["test_list"]
            test_len = len(test)
            # if test_len >= 16:
            #     test = test[:16]
            if "Example usage" in code:
                code = code.split("Example usage")[0]
            if "example usage" in code:
                code = code.split("example usage")[0]
            if metric == "passo":
                test_match_func = problems[task_id]["test_match_function"]
                test_match_func = test_match_func[0]
                my_string = ', '.join(f'"{item}"' for item in test_match_func)
                converted_code = f"{code}"
                
                test_exam = "\nclass Program\n{\n    static bool VerifyStrings(List<string> myList, string targetString)\n    {\n        foreach (var item in myList)\n        {\n            if (!targetString.Contains(item))\n            {\n                return false;\n            }\n        }\n        return true;\n    }\n    static void Main(string[] args) \n    {                \n        List<string> myList = new List<string> {" + f"{my_string}" + "};\n        string targetString = " + f"\"{repr(converted_code)}\";\n        bool result = VerifyStrings(myList, targetString);\n        Debug.Assert(result == true);\n"
                for test_idx in test:
                    test_exam = test_exam + "\n        " + test_idx +";"
                test_exam = test_exam + "\n    }\n}"
            elif metric == "passk":
                test_exam = "class Program {\n    static void Main(string[] args) {"
                for test_idx in test:
                    test_exam = test_exam + "\n        " + test_idx +";"
                test_exam = test_exam + "\n    }\n}"
        elif language == "js":
            test = problems[task_id]["test_list"]
            # test_len = len(test)
            # if test_len >= 31:
            #     test = test[:31]
            if metric == "passo":
                test_match_func = problems[task_id]["test_match_function"]
                test_match_func = test_match_func[0]
                converted_code = f"{code}"
                test_exam = "\nfunction checkStringInList(my_list, target_string) {" + "\n    for (let i = 0; i < my_list.length; i++) {" + "\n        if (!target_string.includes(my_list[i])) {" + "\n            return false;\n        }\n    }\n    return true;\n}\n\n" + f"const my_list = {test_match_func};\nconst target_string = " + f"\"{repr(converted_code)}\";\n"
                
                for test_idx in test:
                    test_exam = test_exam + "\n" + test_idx
                test_exam = test_exam + "\n"
                test_exam = test_exam + "assert.deepEqual(checkStringInList(my_list, target_string), true);\n"
            elif metric == "passk":
                test_exam = ""
                for test_idx in test:
                    test_exam = test_exam + "\n" + test_idx
                test_exam = test_exam + "\n"
        elif language == "php":
            test = problems[task_id]["test_list"]
            test_len = len(test)
            # if test_len >= 31:
            #     test = test[:31]
            if metric == "passo":
                test_match_func = problems[task_id]["test_match_function"]
                test_match_func = test_match_func[0]
                # my_string = ', '.join(f'"{item}"' for item in test_match_func)
                converted_code = f"{code}"
                
                test_exam = "\nfunction validateListInString($my_list, $target_string) {\n    foreach ($my_list as $item) {\n        if (strpos($target_string, $item) === false) {\n            return false;\n        }\n    }\n    return true;\n}"
                test_exam = test_exam + f"\n\n$my_list = {test_match_func};\n$target_string = \"{repr(converted_code)}\";\n$result = validateListInString($my_list, $target_string);\nif ($result !== True)" + "{ throw" + " new Exception(\"Test failed!\"); }\n"
                
                for test_idx in test:
                    if test_idx.endswith("}"):
                        test_exam = test_exam + "\n" + test_idx
                    else:
                        test_exam = test_exam + "\n" + test_idx +";"
                test_exam = test_exam + "\n"
                
            elif metric == "passk":
                test_exam = "\n"
                for test_idx in test:
                    if test_idx.endswith("}"):
                        test_exam = test_exam + "\n" + test_idx
                    else:
                        test_exam = test_exam + "\n" + test_idx +";"
                test_exam = test_exam + "\n"

    # Pre-process for different languages
    if language == "python":
        test_setup = "\n".join(IMPORT_HELPER["python"]) + "\n"
        if metric == "passo":
            test_match_func = problems[task_id]["test_match_function"]
            text = "\n    if len(match_context)==2:\n        match_context1 = match_context[0]\n        match_context2 = match_context[1]\n    else:\n        match_context1 = match_context[0]\n        match_context2 = match_context[0]\n    \n    def context_exists_in_code(context, code):\n        return all(item in code for item in context)\n    if context_exists_in_code(match_context1, code):\n        return True\n    elif context_exists_in_code(match_context2, code):\n        return True\n    else:\n        return False\n"
            match_func = "\ndef match_content():\n" + f"    match_context = {test_match_func}\n" + f"    code = {repr(code)}\n" + text
            
            insert_position = test_func.find("return")
            inserted_content = "if match_content():\n        "
            modified = test_func[:insert_position] + inserted_content + test_func[insert_position:] + "\n    return False"
            
            test_string = test_setup + code + "\n\n" + match_func + "\n\n" + modified + "\n\n" + test_exam + "\n\n" + f"check({entry_point})"
        elif metric == "passk":
            test_string = test_setup + code + "\n\n" + test_func + "\n\n" + test_exam + "\n\n" + f"check({entry_point})"
        
    elif language == "cpp":
        test_set_up = ""
        for s in IMPORT_HELPER["cpp"]:
            if s not in code:
                test_set_up += s + "\n"
        test_string = test_set_up + "\n" + code + "\n" + test_exam
        # print(test_string)
    elif language == "java":
        code = code.replace('public class', 'class')
        test_set_up = ""
        for s in IMPORT_HELPER["java"]:
            if s not in code:
                test_set_up += s + "\n"
        test_string = test_set_up + "\n" + code + "\n" + test_exam
    elif language == "cs":
        # code = code.replace('public class', 'class')
        test_set_up = ""
        for s in IMPORT_HELPER["cs"]:
            if s not in code:
                test_set_up += s + "\n"
        test_string = test_set_up + "\n" + code + "\n" + test_exam
        # print('==========================')
        # print(test_string)
    elif language in ["js", "javascript", "ts", "sh", "go"]:
        if "public " in code:
            code = code.replace("public ","")
        if "static " in code:
            code = code.replace("static ","")
        test_string = code + "\n" + test_exam
        # print('==========================')
        # print(test_string)
    elif language == "go232":
        import_string = problems[task_id]["import"]
        prompt = prompt.replace(import_string, "")
        if example_test and "example_test" in problems[task_id]:
            test = problems[task_id]["example_test"]
        else:
            test = problems[task_id]["test"]
        test_setup = problems[task_id]["test_setup"]
        other_pkgs = []
        for pkg in IMPORT_HELPER["go"]:
            if pkg not in test_setup:
                p = pkg.split("/")[-1]
                if p + "." in code:
                    other_pkgs.append(f"\"{pkg}\"")
        if other_pkgs:
            import_other_pkgs = "import (\n" + "    ".join([p + "\n" for p in other_pkgs]) + ")"
            test_string = test_setup + "\n" + import_other_pkgs + "\n" + prompt + code + "\n" + test
        else:
            test_string = test_setup + "\n" + prompt + code + "\n" + test
    elif language == "rust":
        main = "\nfn main(){ \n } \n"
        declaration = problems[task_id]["declaration"]
        test_string = main + declaration + prompt + code + test
    elif language == "php":
        if code[:5] != "<?php":
            code = "<?php\n" + code
        test_string = code + "\n" + test_exam + "?>"
    return test_string


def stream_jsonl_all(filename: str) -> Iterable[Dict]:
    """
    Streams a JSONL file.
    """
    results = []
    if filename.endswith(".gz"):
        fp = gzip.open(open(filename, "rb"), "rt")
    else:
        fp = open(filename, "r")
    for line in fp:
        # print('=====================================')
        # print(line)
        if any(not x.isspace() for x in line):
            results.append(json.loads(line))
    fp.close()

    return results


def evaluate_functional_correctness(
        input_file: str = None,
        tmp_dir: str = "./",
        n_workers: int = 32,
        timeout: float = 10.0,
        problem_file: str = "",
        out_dir: str = None,
        k: List[int] = [1, 3, 5, 8, 10, 12, 15, 100],
        test_groundtruth: bool = False,
        example_test: bool = False,
        is_mbpp: bool = False,
        language: str = "python",
        metric: str = "passo",
):
    """
    Evaluates the functional correctness of a model.
    """
    if example_test:
        print("Example test...")

    problems = read_dataset(problem_file,
                            dataset_type="data")
    sample_jsonl = stream_jsonl_all(input_file)


    with ThreadPoolExecutor(max_workers=n_workers) as executor:

        futures = []
        completion_id = Counter()
        n_samples = 0
        results = defaultdict(list)

        if test_groundtruth:
            # print("Testing ground truth...")
            for sample in tqdm(problems.values()):
                task_id = sample["task_id"]
                lang = task_id.split("/")[0].lower()
                if lang == "javascript":
                    lang = "js"
                tmp_dir_ = os.path.join(tmp_dir, lang, "evaluation")
                sample["generation"] = sample["canonical_solution"]
                sample["test_code"] = process_humaneval_test(sample, problems, example_test, language, metric)
                if sample["test_code"] is None:
                    continue
                args = (task_id, sample, lang, timeout, tmp_dir_, completion_id[task_id])
                future = executor.submit(check_correctness, *args)
                futures.append(future)
                completion_id[task_id] += 1
                n_samples += 1
        else:
            print("Reading samples...")
            for sample in tqdm(sample_jsonl):
                task_id = sample["task_id"]
                if not is_mbpp:
                    lang = language
                if not is_mbpp and lang == "javascript":
                    lang = "js"
                if is_mbpp:
                    lang = "python"
                tmp_dir_ = os.path.join(tmp_dir, lang, "evaluation")
                sample["task_id"] = task_id
                sample["test_code"] = process_humaneval_test(sample, problems, example_test, is_mbpp, language, metric)
                if sample["test_code"] is None:
                    continue
                if "completion_id" in sample:
                    completion_id_ = sample["completion_id"]
                else:
                    completion_id_ = completion_id[task_id]
                args = (task_id, sample, lang, timeout, tmp_dir_, completion_id_)
                future = executor.submit(check_correctness, *args)
                futures.append(future)
                completion_id[task_id] += 1
                n_samples += 1

        if len(completion_id) == len(problems):
            evaluate_pass_at_k = True
        else:
            evaluate_pass_at_k = False

        print("Running test suites...")
        for future in tqdm(as_completed(futures), total=len(futures)):
            result = future.result()
            results[result["task_id"]].append((result["completion_id"], result))

    # Calculate pass@k.
    total, correct = [], []
    for result in results.values():
        passed = [r[1]["passed"] for r in result]
        total.append(len(passed))
        correct.append(sum(passed))
    total = np.array(total)
    correct = np.array(correct)
    if evaluate_pass_at_k:
        ks = k
        pass_at_k = {f"pass@{k}": estimate_pass_at_k(total, correct, k).mean()
                     for k in ks if (total >= k).all()}
        print(pass_at_k)
    else:
        print("Total:", np.sum(total))
        print("Correct:", np.sum(correct))
    return pass_at_k
