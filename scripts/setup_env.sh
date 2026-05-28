# scripts/setup_env.sh

#!/bin/bash

echo "=================================="
echo " Setting Up ADMFL Environment "
echo "=================================="

echo "[1] Creating virtual environment..."
python3 -m venv admfl_env

echo "[2] Activating virtual environment..."
source admfl_env/bin/activate

echo "[3] Upgrading pip..."
pip install --upgrade pip

echo "[4] Installing project dependencies..."
pip install -r requirements.txt

echo "[5] Creating required directories..."

mkdir -p logs
mkdir -p results
mkdir -p datasets/raw
mkdir -p datasets/processed

echo "[6] Environment setup completed."

echo "=================================="
echo " ADMFL Ready to Run "
echo "=================================="