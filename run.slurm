#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --output=output.log
#SBATCH --time=1:00:00

echo "Starting job at $(date)"


# Load the virtual environment
source venv36/bin/activate

echo "Virtual environment activated"

# Execute the script
python3 parameter_analysis.py
echo "Job finished at $(date)"
