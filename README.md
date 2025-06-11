## 1. Introduction

We provide a test script to evaluate the performance of the **Phi3-medium-4k-instruct** model on code generation benchmarks.



## 2. Setup

```
pip install accelerate
pip install attrdict
pip install transformers
pip install pytorch
```

## 3. Add new test case

We provide a script that uses a large language model to automatically add test cases.

```bash
cd $current_dir
bash Auto_add_cases/exam_run.sh
```


## 4. Evaluation

We've created a sample script, **main_example.sh**, that demonstrates how to test the **Phi3_medium_4k_instruct** model on the MultiOOP dataset leveraging **8** GPUs. If your use case involves a different model, simply adjust the script to fit your needs.

```bash
cd $current_dir
bash main_example.sh
```

To evaluate the **Phi3_medium_4k_instruct** model separately, please follow the script below:

```bash
cd $current_dir
bash slurm_run_main.sh
```
