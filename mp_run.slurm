#!/bin/bash
#SBATCH --job-name=loganalysis.job
#SBATCH --output=.out/log2018.out
#SBATCH --error=.out/log2018.err
#SBATCH --time=2:00:00


echo "Starting job at $(date)"


# Load the virtual environment
source venv36/bin/activate

echo "Virtual environment activated"

# Execute the script
python3 multi_process.py
echo "Job finished at $(date)"

