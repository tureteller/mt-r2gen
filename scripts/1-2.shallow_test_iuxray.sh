#!/bin/bash

dataset="iu_xray"
annotation="data/iu_xray/annotation.json"
base_dir="./data/iu_xray/images"
delta_file="/data/tmp_ymy/R2GenGPT/save/iu_xray/v1_shallow/checkpoints/checkpoint_epoch8_step2322_bleu0.148901_cider0.463472.pth"

version="v1_shallow"
savepath="./save/$dataset/$version"

python -u train.py \
    --test \
    --dataset ${dataset} \
    --annotation ${annotation} \
    --base_dir ${base_dir} \
    --delta_file ${delta_file} \
    --test_batch_size 16 \
    --freeze_vm True \
    --vis_use_lora False \
    --savedmodel_path ${savepath} \
    --max_length 60 \
    --min_new_tokens 40 \
    --max_new_tokens 100 \
    --repetition_penalty 2.0 \
    --length_penalty 2.0 \
    --num_workers 8 \
    --devices 1 \
    2>&1 |tee -a ${savepath}/log.txt