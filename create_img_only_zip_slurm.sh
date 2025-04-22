#!/usr/bin/env bash

#SBATCH --job-name=zip_data_img_only
#SBATCH -n 12
#SBATCH --time=120:00:00
#SBATCH --mem-per-cpu=2000
#SBATCH --gpus=1
#SBATCH --tmp=208000

module load eth_proxy

python create_img_only_zip.py 