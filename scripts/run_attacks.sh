# scripts/run_attacks.sh

#!/bin/bash

echo "================================="
echo " Running ADMFL Attack Scenarios "
echo "================================="

echo "[1] Launching DDoS Attack..."
python attacks/ddos_attack.py

echo "[2] Launching Spoofing Attack..."
python attacks/spoofing_attack.py

echo "[3] Launching Poisoning Attack..."
python attacks/poisoning_attack.py

echo "[4] Launching Swarm Attack..."
python attacks/swarm_attack.py

echo "================================="
echo " All Attack Simulations Completed "
echo "================================="