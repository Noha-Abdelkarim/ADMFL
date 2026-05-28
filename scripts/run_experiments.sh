# scripts/run_experiments.sh

#!/bin/bash

echo "======================================="
echo " Starting ADMFL Experimental Pipeline "
echo "======================================="

CONFIG_FILE="config.yaml"

echo "[1] Starting ADMFL Framework..."
python run.py --config $CONFIG_FILE

echo "[2] Running Federated Learning..."
python tafl/fl_server.py

echo "[3] Launching DDoS Attack Scenario..."
python attacks/ddos_attack.py

echo "[4] Launching Spoofing Attack Scenario..."
python attacks/spoofing_attack.py

echo "[5] Evaluating Framework Performance..."
python evaluation/metrics.py

echo "[6] Generating Visualizations..."
python visualization/plot_metrics.py

echo "======================================="
echo " ADMFL Experimental Pipeline Completed "
echo "======================================="