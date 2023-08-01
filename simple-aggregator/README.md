## Metronome Take-home Code Screen

This package contains the solution to the problem.
It is written in python leveraging the `pandas` package for data manipulations.

It will output hourly aggregated events as a dictionary, based on the given input parameters.
For E.g.:
```commandline
{
 '2021-3-1:T5:00:00': 12, 
 '2021-5-1:T3:00:00': 1, 
 '2022-3-1:T4:00:00': 22, 
 '2022-3-1:T14:00:00': 9, 
 '2022-3-2:T5:00:00': 54
 }
```

### Contents
- root dir: `simple-aggregator`
  - README.md - this file
  - source: `aggregator.py`
  - requirements: `requirements.txt` - dependencies
  - data dir: `data`   - contains event data .csv files
  - tests dir: `tests` - unit tests

### Install
- Install python3, if not installed already
- Install dependencies - from root dir run,
    
  `pip install -r requirements.txt`
- This will install pandas, pytest, dateutil and their dependencies.

### Run Application
From root dir, you can run the application with this command line:

 `% pyton3 aggregator.py -h` or just `> aggregator.py -h`

Should display the following usage details:
```commandline
  usage: aggregator.py [-h] [-c CUST_ID] [-f FILE_PATH] [-fd FROM_DATE] [-td TO_DATE]
  
  Aggregates events into hourly buckets.
  
  optional arguments:
    -h, --help            show this help message and exit
    -c CUST_ID, --cust_id CUST_ID
                          customer id to query for events
    -f FILE_PATH, --file_path FILE_PATH
                          path to file with events data
    -fd FROM_DATE, --from_date FROM_DATE
                          start date for query (YYYY-MM-DD:THH:MM:SS:00Z)
    -td TO_DATE, --to_date TO_DATE
                          start date for query (YYYY-MM-DD:THH:MM:SS:00Z)
```
Example:
```commandline
   python3 aggregator.py -c b4f9279a0196e40632e947dd1a88e857 -f /Users/rajeshfamily/work/simple-aggregator/data/test2.csv 
  -fd 2022-03-01T01:00:00Z -td 2022-03-01T05:00:00Z
```
### Running Unit tests

Unit tests can be run from the root dir with the following command:

`% python3 -m pytest tests -v `







