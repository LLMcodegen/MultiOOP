
#!/bin/bash
cd $current_dir
MODEL_NAME_OR_PATH= $model_path
SAVA_PATH="./result_output_cpp/Phi3_medium_4k_instruct_T_08_cpp_passo.jsonl"

DATASET_ROOT="./data/"
LANGUAGE="cpp"
TEMP="0.8"
K="15"
SUB_DIR="metrics"
# get directory path from the save path
DIR_PATH=$(dirname "$SAVA_PATH")
# get the base name of the save path
FILE_NAME=$(basename "$SAVA_PATH")
METRICS_PATH="$DIR_PATH/$SUB_DIR/$FILE_NAME"

python eval_pal.py \
    --logdir ${MODEL_NAME_OR_PATH} \
    --logfilepath ${SAVA_PATH} \
    --k_sample ${K} \
    --temperature ${TEMP} \
    --language ${LANGUAGE} \
    --dataroot ${DATASET_ROOT} \
    --metrics_path ${METRICS_PATH} \
    --metrics passo

