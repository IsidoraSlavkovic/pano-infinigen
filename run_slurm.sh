#!/usr/bin/env bash

#SBATCH -n 12
#SBATCH --time=120:00:00
#SBATCH --mem-per-cpu=20000
#SBATCH --gpus=4
#SBATCH --gres=gpumem:18000m
#SBATCH --job-name=pano-infinigen_0_24
#SBATCH --tmp=208000

module load eth_proxy

name=pano-infinigen_0_24
id=03790512 #03790512 #02691156 #03790512 #02958343
num_scenes=25
num_concurrent=100

python -m infinigen.datagen.manage_jobs --output_folder outputs/my_indoor_dataset_0_24 --num_scenes $num_scenes --pipeline_configs local_256GB.gin monocular.gin blender_gt.gin indoor_background_configs.gin \
    --configs singleroom.gin fast_solve.gin \
    --pipeline_overrides get_cmd.driver_script='infinigen_examples.generate_indoors' manage_datagen_jobs.num_concurrent=$num_concurrent \
    --overrides compose_indoors.restrict_single_supported_roomtype=True \
    --wandb_mode online