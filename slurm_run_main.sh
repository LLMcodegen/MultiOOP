#!/bin/bash
cd $current_dir

# The evaluation results are stored in the `./metric_cpp` folder.
python main_run.py \
    --sample_file ./result_output_cpp/Phi3_medium_4k_instruct_T_08_cpp_passo.jsonl \
    --data_root ./data \
    --lang cpp \
    --metric passo