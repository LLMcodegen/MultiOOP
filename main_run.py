from multi_oop.evaluation import evaluate_functional_correctness
import fire
import sys
import os
import json
# from read_jsonl import read_jsonl_main

def entry_point(
    sample_file: str,
    data_root: str,
    lang: str = "python",
    metric: str = "passo",
    pro: str = "few"
):
    """
    Evaluates the functional correctness of generated samples, and writes
    results to f"{sample_file}_results.jsonl.gz"
    """
    timeout = 10
    runlang = lang
    log_dir = "./metric_cpp"

    res = evaluate_functional_correctness(input_file=sample_file, problem_file=os.path.join(data_root, f"oop-{lang}.jsonl"), tmp_dir=log_dir, timeout=timeout, language=runlang, metric=metric)
    print('---------------------------------')
    print("score is", res)
    print('=========================')
    file_path = os.path.join("./metric_cpp", sample_file.split('/')[-1])
    with open(file_path, 'w') as file:
        json.dump(res, file)

def main():
    fire.Fire(entry_point)

sys.exit(main())

