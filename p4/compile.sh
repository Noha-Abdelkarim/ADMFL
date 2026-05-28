# p4/compile.sh

#!/bin/bash

echo "=================================="
echo " Compiling ADMFL P4 Program "
echo "=================================="

P4_FILE="admfl_switch.p4"
OUTPUT_DIR="build"

mkdir -p $OUTPUT_DIR

echo "[1] Compiling P4 source..."

p4c-bm2-ss \
    --p4v 16 \
    --p4runtime-files $OUTPUT_DIR/admfl_switch.p4info.txt \
    -o $OUTPUT_DIR/admfl_switch.json \
    $P4_FILE

if [ $? -eq 0 ]; then

    echo "[2] Compilation successful."

else

    echo "[ERROR] P4 compilation failed."

    exit 1
fi

echo "[3] Generated files:"
echo " - $OUTPUT_DIR/admfl_switch.json"
echo " - $OUTPUT_DIR/admfl_switch.p4info.txt"

echo "=================================="
echo " ADMFL P4 Build Completed "
echo "=================================="