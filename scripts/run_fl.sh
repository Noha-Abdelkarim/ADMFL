# scripts/run_fl.sh

#!/bin/bash

echo "================================="
echo " Starting Federated Learning "
echo "================================="

echo "[1] Starting FL Server..."
python tafl/fl_server.py

echo "[2] Starting FL Clients..."
python tafl/fl_client.py

echo "================================="
echo " Federated Learning Completed "
echo "================================="