#!/usr/bin/env bash

#SBATCH --job-name=train_test_split
#SBATCH -n 12
#SBATCH --time=120:00:00
#SBATCH --mem-per-cpu=2000
#SBATCH --gpus=1
#SBATCH --tmp=208000

module load eth_proxy

python train_test_split.py