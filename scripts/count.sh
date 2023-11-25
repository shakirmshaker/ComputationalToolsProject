#!/bin/sh

# Script to count number of records in current directory
# Usage ./count.sh

echo -e "Record counts:"
for file in *properties.json; do
    echo -e "- File $file records: $(cat $file | grep -n 'pageProps' | wc -l)"
done