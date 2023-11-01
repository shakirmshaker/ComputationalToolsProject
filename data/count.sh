#!/bin/sh

echo -e "Record counts:"
for file in *properties.json; do
    echo -e "File $file records: $(cat $file | grep -n 'pageProps' | wc -l)"
done