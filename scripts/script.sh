#!/bin/sh

# Script for collecting addresses from specified municipalities or crawling properties using address files.

# Usage:
#   -m: Run for the specified municipalities
#   -p: Crawl properties using address files
#
# Example usage:
#   ./script.sh -m  # Collect addresses from municipalities
#   ./script.sh -p  # Crawl properties using address files

while getopts ":mp" opt; do
    case $opt in
        m)
            municipalities=("Gribskov" "Fredensborg" "Furesø" "Rødovre" "Brøndby" "Halsnæs" "Albertslund" "Herlev" "Hørsholm" "Allerød" "Glostrup" "Ishøj" "Vallensbæk" "Dragør")

            for municipality in "${municipalities[@]}"; do
                echo "Collecting addresses from municipality of $municipality..."
                python main.py $municipality
            done
        ;;
        p)
            address_files=(*_addresses.json)
            
            for file_addresses in "${address_files[@]}"; do
                echo "Crawling properties using $file_addresses..."
                nohup python main.py $file_addresses &
            done
        ;;
        \?)
            echo "Invalid option: -$OPTARG. Use -m for municipalities or -p for properties." >&2
            exit 1
        ;;
    esac
done