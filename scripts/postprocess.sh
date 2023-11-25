#!/bin/sh

# Script that processes property information stored in JSON files within a specified directory. It runs the 'main.py' script with the -p option for each file matching the pattern *_properties.json.
# Usage:
#   ./script.sh <directory>
# Note: Provide the directory containing the JSON files as a command-line argument.

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
