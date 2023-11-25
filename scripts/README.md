# Scripts

These are some scripts we used to automate the crawling and collect record information afterwards.

```bash
.
|-- count.sh            # Script to count number of records in current directory
|-- postprocess.sh      # Script that processes property information stored in JSON files within a specified directory. It runs the 'main.py' script with the -p option for each file matching the pattern *_properties.json.
`-- script.sh           # Script for collecting addresses from specified municipalities or crawling properties using address files. This is the main script used for crawling.
```