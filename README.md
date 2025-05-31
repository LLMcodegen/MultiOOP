## 1. Introduction

We provide a test script to evaluate the performance of the **Phi3-medium-4k-instruct** model on code generation benchmarks.



## 2. Setup

```
pip install accelerate
pip install attrdict
pip install transformers
pip install pytorch
```


## 3. Evaluation

We've created a sample script, **eval.sh**, that demonstrates how to test the **DeepSeek-Coder-1.3b-Base** model on the MultiOOP dataset leveraging **8** GPUs. If your use case involves a different model, simply adjust the script to fit your needs.

Additionally, for various programming languages, the execution path may differ. Please ensure you update the appropriate paths in the **humaneval/execution.py** file accordingly.

```bash
MODEL_NAME_OR_PATH="deepseek-ai/deepseek-coder-1.3b-base"
DATASET_ROOT="data/"
LANGUAGE="python"
python -m accelerate.commands.launch --config_file test_config.yaml eval_pal.py --logdir ${MODEL_NAME_OR_PATH} --language ${LANGUAGE} --dataroot ${DATASET_ROOT} 
```

To evaluate the instruction-based model, please follow the script below:
```bash
LANG="python"
OUPUT_DIR="output"
MODEL="deepseek-coder-33b-instruct"

python eval_instruct.py \
    --model "deepseek-ai/$MODEL" \
    --output_path "$OUPUT_DIR/${LANG}.$MODEL.jsonl" \
    --language $LANG \
    --temp_dir $OUPUT_DIR
```

## 4. Experimental Results

We report experimental results here for 8 main-stream programming languages, **python**, **c++**, **java**, **PHP**, **TypeScript**, **C#**, **Bash**, and **JavaScript**. For all open-source models, we utilize this repository to obtain the performance of the models on the HumanEval dataset. We set the maximum input length to **4096** and the maximum output length to **500**, and employ the **greedy search strategy**.

