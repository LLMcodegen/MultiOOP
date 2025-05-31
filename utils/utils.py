import re

languge_settings = {
    'python': {
        'full_name': 'Python',
        'indent': 4,
    },
    'cpp': {
        'full_name': 'cpp',
        'indent': 0,
        'main': "int main()",
    },
    'java': {
        'full_name': 'Java',
        'indent': 4,
        'main': "public static void main",
    },
    'cs': {
        'full_name': "csharp",
        'indent': 0,
        'main': "public static void Main",
    },
    'php': {
        'full_name': "PHP",
        'indent': 0,
    },
    'ts': {
        'full_name': "TypeScript",
        'indent': 0,
    },
    'js': {
        'full_name': "JavaScript",
        'indent': 0
    },
    'sh': {
        'full_name': "Bash",
        'indent': 0
    }
}

def get_function_name(question: str, lang: str):
    func_lines = [x for x in question.strip().split('\n') if x.strip()]

    if lang.lower() == 'python':
        func_idx = [i for i in range(len(func_lines)) if func_lines[i].startswith("def ")][-1]
        func_name = func_lines[func_idx].split('(')[0].strip()
        func_prefix = "\n".join(func_lines[:func_idx])
        return func_name, func_prefix
    
    func_name = func_lines[-1].split('{')[0].strip()
    func_prefix = "\n".join(func_lines[:-1])
    return func_name, func_prefix

def extract_generation_code(example: str, lang_code: str, verbose: bool=False):
    task_id = example['task_id']
    output = example.get('output', example.get("gpt_completion"))
    question = example["prompt"].strip()
    setting = languge_settings[lang_code]
    lang = setting['full_name']
    indent = setting['indent']

    try:
        code_block: str = re.findall(f'```{lang.lower()}\n(.*?)```', output, re.DOTALL | re.IGNORECASE)[0]
        if verbose:
            print(">>> Task: {}\n{}".format(task_id, code_block))
        
        # Remove main
        if setting.get('main', None) and setting['main'] in code_block:
            main_start = code_block.index(setting['main'])
            code_block = code_block[:main_start]
        
        func_name, func_prefix = get_function_name(question, lang)

        try:
            start = code_block.lower().index(func_name.lower())
            indent = 0
            while start - indent >= 0 and code_block[start - indent-1] == ' ':
                indent += 1
            
            try:
                end = code_block.rindex('\n' + ' '*indent + '}')
            except:
                end = len(code_block)
        except:
            start = 0
            try:
                end = code_block.rindex('\n' + ' '*indent + '}')
            except:
                end = len(code_block)

        body = code_block[start:end]

        if lang_code.lower() in ['php', 'ts', 'js']:
            body += '\n' + ' '*indent + '}'
    
        generation = func_prefix + '\n' + body + '\n'
        example['generation'] = generation

    except Exception as ex:
        print("Failed to extract code block with error `{}`:\n>>> Task: {}\n>>> Output:\n{}".format(
            ex, task_id, output
        ))
        example['generation'] = example['prompt'] + '\n' + output
    
    return example

def cleanup_code(
    code: str,
    language_type: str = None,
    dataset: str = None,
    issft: bool = False,
    stop_words = [],
    pro: str = None
):
    """
    Cleans up the generated code.
    """

    if language_type.lower() == "python":
        if issft:
            code = _clean_python_code_for_sft(code)
        stop_words_begin = ["```python", "```Python"]
        stop_words_end = ["# Example usage", "```"]
        if pro == "cot":
            pattern1 = r"```python\n([\s\S]*?)\n```"
            pattern2 = r"```Python\n([\s\S]*?)\n```"
            pattern3 = r"```PYTHON\n([\s\S]*?)\n```"
            code = _truncate_code_at_stopwords_cot(code, pattern1, pattern2, pattern3, stop_words_begin, stop_words_end, language_type.lower())
        else:
            code = _truncate_code_at_stopwords(code, stop_words_begin, stop_words_end, language_type.lower())
    elif language_type.lower() == "ts":
        code = _truncate_code_at_stopwords(code, stop_words + ["\nexport", "\nimport", "\nexport default", "\nimport default", "\nconsole.log"])
    elif language_type.lower() == "java":
        stop_words_begin = ["```java", "```Java"]
        stop_words_end = ["```"]
        if pro == "cot":
            pattern1 = r"```java\n([\s\S]*?)\n```"
            pattern2 = r"```Java\n([\s\S]*?)\n```"
            pattern3 = r"```JAVA\n([\s\S]*?)\n```"
            code = _truncate_code_at_stopwords_cot(code, pattern1, pattern2, pattern3, stop_words_begin, stop_words_end, language_type.lower())
        else:
            code = _truncate_code_at_stopwords(code, stop_words_begin, stop_words_end, language_type.lower())
    elif language_type.lower() == "cpp":
        stop_words_begin = ["```cpp", "```c++", "```C++", "```CPP"]
        stop_words_end = ["int main() {", "```"]
        if pro == "cot":
            pattern1 = r"```cpp\n([\s\S]*?)\n```"
            pattern2 = r"```Cpp\n([\s\S]*?)\n```"
            pattern3 = r"```c++\n([\s\S]*?)\n```"
            code = _truncate_code_at_stopwords_cot(code, pattern1, pattern2, pattern3, stop_words_begin, stop_words_end, language_type.lower())
        else:
            code = _truncate_code_at_stopwords(code, stop_words_begin, stop_words_end, language_type.lower())
    elif language_type.lower() == "php":
        stop_words_begin = ["```php", "```Php", "```PHP"]
        stop_words_end = ["}\n```", "```"]
        if pro == "cot":
            pattern1 = r"```php\n([\s\S]*?)\n```"
            pattern2 = r"```Php\n([\s\S]*?)\n```"
            pattern3 = r"```PHP\n([\s\S]*?)\n```"
            code = _truncate_code_at_stopwords_cot(code, pattern1, pattern2, pattern3, stop_words_begin, stop_words_end, language_type.lower())
        else:
            code = _truncate_code_at_stopwords(code, stop_words_begin, stop_words_end, language_type.lower())
    elif language_type.lower() == "js":
        stop_words_begin = ["```javascript", "```Javascript", "```JavaScript"]
        stop_words_end = ["Example usage", "```"]
        if pro == "cot":
            pattern1 = r"```javascript\n([\s\S]*?)\n```"
            pattern2 = r"```Javascript\n([\s\S]*?)\n```"
            pattern3 = r"```JavaScript\n([\s\S]*?)\n```"
            code = _truncate_code_at_stopwords_cot(code, pattern1, pattern2, pattern3, stop_words_begin, stop_words_end, language_type.lower())
        else:
            code = _truncate_code_at_stopwords(code, stop_words_begin, stop_words_end, language_type.lower())
    elif language_type.lower() == "cs":
        stop_words_begin = ["```csharp", "```c#"]
        stop_words_end = ["```"]
        # print('===========================')
        # print(code)
        if pro == "cot":
            pattern1 = r"```csharp\n([\s\S]*?)\n```"
            pattern2 = r"```Csharp\n([\s\S]*?)\n```"
            pattern3 = r"```c#\n([\s\S]*?)\n```"
            code = _truncate_code_at_stopwords_cot(code, pattern1, pattern2, pattern3, stop_words_begin, stop_words_end, language_type.lower())
        else:
            code = _truncate_code_at_stopwords(code, stop_words_begin, stop_words_end, language_type.lower())
        # code = _truncate_code_at_stopwords(code, stop_words_begin, stop_words_end, language_type.lower())
    else:
        code = _truncate_code_at_stopwords(code, stop_words)
    return code

def _clean_python_code_for_sft(code):
    code = code.replace("\r", "")
    if "```python" in code:
        code_start_idx = code.index("```python")
        code = code[code_start_idx:].replace("```python", "").strip()
        end_idx = code.find("```") if "```" in code else len(code)
        code = code[:end_idx].strip()

    return code

def _truncate_code_at_stopwords_cot(code, pattern1, pattern2, pattern3, stop_words_begin, stop_words_end, language):
    try:
        code_blocks = re.findall(pattern1, code)
        if len(code_blocks) == 0:
            code_blocks = re.findall(pattern2, code)
            if len(code_blocks) == 0:
                print('============================')
                print(pattern3)
                print(code)
                code_blocks = re.findall(pattern3, code)
                if len(code_blocks) == 0:
                    for stop_word in stop_words_begin:
                        index = code.rfind(stop_word)
                        if index != -1:
                            code = code[index + len(stop_word):]
                            break
                else:
                    code = max(code_blocks, key=len)
            else:
                code = max(code_blocks, key=len)
        else:
            code = max(code_blocks, key=len)
    except:
        for stop_word in stop_words_begin:
            index = code.rfind(stop_word)
            if index != -1:
                code = code[index + len(stop_word):]
                break
    for stop_word in stop_words_begin:
        index = code.rfind(stop_word)
        if index != -1:
            code = code[index + len(stop_word):]
            break
    if "<?php" in code:
        code = code.split("<?php")[1]
    for stop_word in stop_words_end:
        if stop_word in code:
            code = code.split(stop_word)[0]
            break
    return code
    
def _truncate_code_at_stopwords(code, stop_words_begin, stop_words_end, language):
    min_stop_idx = len(code)
    if language == 'php':
        for stop_word in stop_words_begin:
            if stop_word in code:
                code = code.split(stop_word)[1]
                break
        if "<?php" in code:
            code = code.split("<?php")[1]
        
        for stop_word in stop_words_end:
            if stop_word in code:
                code = code.split(stop_word)[0]
                break    
        
        last_index = code.rfind("\n}")
        if last_index != -1:
            code = code[:last_index + 2]
    else:
        for stop_word in stop_words_begin:
            if stop_word in code:
                code = code.split(stop_word)[1]
                break
        for stop_word in stop_words_end:
            if stop_word in code:
                code = code.split(stop_word)[0]
                break
    return code 
    # for stop_word in stop_words:
    #     stop_index = code.find(stop_word)
    #     if 0 <= stop_index < min_stop_idx:
    #         min_stop_idx = stop_index
    # return code[:min_stop_idx]