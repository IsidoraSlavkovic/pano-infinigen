#!/usr/bin/env bash

#SBATCH --job-name=pano-infinigen-array100
#SBATCH --array=1-100
#SBATCH -n 12
#SBATCH --time=4:00:00
#SBATCH --mem-per-cpu=20000
#SBATCH --gpus=1
#SBATCH --tmp=208000

echo "$(date) start ${SLURM_JOB_ID}"

module load eth_proxy

name=pano-infinigen-array100
# id=${SLURM_JOB_ID} #03790512 #02691156 #03790512 #02958343
num_scenes=1
num_concurrent=32
folder_name="${SLURM_JOB_ID}_${SLURM_ARRAY_TASK_ID}"

python -m infinigen.datagen.manage_jobs --output_folder outputs/indoor/$folder_name --num_scenes $num_scenes --pipeline_configs local_256GB.gin monocular.gin blender_gt.gin indoor_background_configs.gin \
    --configs singleroom.gin fast_solve.gin \
    --pipeline_overrides get_cmd.driver_script='infinigen_examples.generate_indoors' manage_datagen_jobs.num_concurrent=$num_concurrent \
    --overrides compose_indoors.restrict_single_supported_roomtype=True \
    --wandb_mode online