#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

DIRECTORY=$1

for FILE in "$DIRECTORY"/*_properties.json; do
    if [ ! -f "$FILE" ]; then
        continue
    fi
    python main.py -p "$FILE"

done

echo "Processing complete."
