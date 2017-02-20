#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=0-1:00:00

# Load required modules
module load Python/2.7.11-GCC-4.9.2

# Run our python script (and measure how long it takes)
time python pi_1.py