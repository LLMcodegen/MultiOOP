import os
from openai import OpenAI
import subprocess
import random
import argparse

# gpt-3.5-turbo
# gpt-4o-mini

def model_run(prompt):
    sys_prompt = ""
    client = OpenAI(base_url="url", api_key="api-key")
    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_tokens = 1024,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}])
    return completion.choices[0].message.content

def prompt_func(python_code, test_case):
    init_prompt = "You are a skilled Python programmer. Based on the test cases provided in the Python code, generate one new and unique test cases. Ensure that these new test cases cover a variety of scenarios, edge cases, and input types to improve the diversity and comprehensiveness of the testing. Avoid duplicating any existing test cases.\n```python\n"
    prompt = init_prompt + python_code + "\n# Test cases\n" + test_case + "\n```\nImportantly, the format of the newly generated test cases must remain consistent with the existing test cases."
    return prompt

def format_template(answer):
    if "```python" in answer:
        answer = answer.split("```python")[1]
    if "```" in answer:
        answer = answer.split("```")[0]
    return answer.strip()

def read_file(folder_path):
    files =[]
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            file_path = os.path.join(folder_path, filename)
            files.append(file_path)
    return files

def write_file(file_path, answer):
    with open(file_path, 'a') as write_file:
        write_file.write(answer)

# Clean up blank lines in code
def clean_func(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    non_empty_lines = [line for line in lines if line.strip()]
    with open(file_path, 'w') as file:
        file.writelines(non_empty_lines)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        filtered_lines = [line for line in lines if not line.strip().startswith('# ')]
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

# Generate new test case
def generate_case(file_path):
    print(f"\nReading file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    filtered_code = []
    filtered_case = []
    for line in lines:
        if line.strip().startswith('print'):
            filtered_case.append(line)
        else:
            filtered_code.append(line)
    print('------------------------------------')
    python_code = "".join(filtered_code)
    test_case = "".join(filtered_case)
    prompt = prompt_func(python_code, test_case)
    response = model_run(prompt)
    answer = format_template(response)
    write_file(file_path, answer)

# Test test case and delete those that do not conform
def delete_case(file_path, results):
    len_n = len(results)
    false_indices = [i for i, val in enumerate(results) if not val]
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    filtered_code = []
    filtered_case = []
    number = 0
    for line in lines:
        if line.strip().startswith('print'):
            if (number not in false_indices) and (number < len_n):
                filtered_case.append(line)
            number = number + 1
        else:
            filtered_code.append(line)
    with open(file_path, 'w') as file:
        file.writelines(filtered_code)
    with open(file_path, 'a') as write_file:
        write_file.writelines(filtered_case)
    
def run_case(file_path):
    result = subprocess.run(["python", file_path], capture_output=True, text=True)    
    output_lines = result.stdout.strip().split('\n')
    results = [line == 'True' for line in output_lines]
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    number = 0
    for line in lines:
        if line.strip().startswith('print'):
            number = number + 1
        
    if (False in results) or (len(results) < number):
        delete_case(file_path, results)

def cat_case(file_path, case_n):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    filtered_code = []
    filtered_case = []
    number = 0
    for line in lines:
        if line.strip().startswith('print'):
            if number < case_n:
                filtered_case.append(line)
            number = number + 1
        else:
            filtered_code.append(line)
    with open(file_path, 'w') as file:
        file.writelines(filtered_code)
    with open(file_path, 'a') as write_file:
        write_file.writelines(filtered_case)
    print("Current number of examples:", number)
    if (case_n - number)<= 0:
        return True
    return False

def main(folder_path, case_n):
    files = read_file(folder_path)
    for file_path in files:
        count_n = 0
        while True:
            # 1. Clean up blank lines in code
            clean_func(file_path)
            # 2. View the number of test cases
            if cat_case(file_path, case_n) or count_n > case_n:
                break
            # 3. Generate new test case
            generate_case(file_path)
            # 4. Clean up blank lines in code
            clean_func(file_path)
            # 5. Test new test case
            run_case(file_path)
            count_n = count_n + 1

def arg_main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder_path", type=str, default="./MultiOOP/Auto_add_cases/sample")
    parser.add_argument("--case_n", type=int, default=20)
    args = parser.parse_args()
    return args
if __name__ == '__main__':
    args = arg_main()
    folder_path = args.folder_path
    case_n = args.case_n
    main(folder_path, case_n)
