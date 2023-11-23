#!/bin/bash

while getopts ":mp" opt; do
    case $opt in
        m)
            # Run for the following municipalities
            # Rerun to gather more data
            municipalities=("Gribskov" "Fredensborg" "Furesø" "Rødovre" "Brøndby" "Halsnæs" "Albertslund" "Herlev" "Hørsholm" "Allerød" "Glostrup" "Ishøj" "Vallensbæk" "Dragør")
            # municipalities=("Gribskov")

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