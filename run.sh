#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH --qos=normal
#SBATCH --job-name=LUT
#SBATCH --output=LUT.out
#SBATCH --time 0-1:00

START=$(date)
mpiexec nrniv -mpi -quiet -python run_network.py
END=$(date)


echo "Done running model at $(date)"