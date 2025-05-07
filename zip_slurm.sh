#!/usr/bin/env bash

#SBATCH --job-name=zip_data
#SBATCH -n 12
#SBATCH --time=120:00:00
#SBATCH --mem-per-cpu=2000
#SBATCH --gpus=1
#SBATCH --tmp=208000

module load eth_proxy

zip -r -0 /cluster/work/igp_psr/infinigen_outdoor_1000s_part4.zip /cluster/work/igp_psr/islavkovic/pano-infinigen/outputs/outdoor
