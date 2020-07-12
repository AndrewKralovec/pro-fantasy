# pro-fantasy
pro-football-reference.com web scraper. 
Python web scraper for www.pro-football-reference.com (currenlty). Exports data in console, csv, and pdf formate (using pure python).

## Quick-Start Guide

- [Installation](#installation)
- [Usage](#usage)

### Installation

**1. Clone this repo:**

```sh
git clone --depth 1 https://github.com/AndrewKralovec/pro-fantasy.git my-app
cd my-app
```


**2. Remove project git files:**

```sh
rm -rf .git && git init
```


**3. Install the dependencies:**

```sh
pip install -r requirements.txt
```

> Dependencies done installing!
> You're now setup

## Usage
```sh
python ./main.py
```

- (Optional), run with docker. 
```sh
docker-compose up
```
help
```sh
python .\main.py --help
usage: main.py [-h] [--output {csv,console,pdf}] [--file_name FILE_NAME]
               [--year_min YEAR_MIN] [--year_max YEAR_MAX]
               [--pos POS [POS ...]] [--game_num_min GAME_NUM_MIN]
               [--game_num_max GAME_NUM_MAX] [--week_num_min WEEK_NUM_MIN]
               [--week_num_max WEEK_NUM_MAX] [--order_by ORDER_BY]

optional arguments:
  -h, --help            show this help message and exit
  --output {csv,console,pdf}
                        output format type
  --file_name FILE_NAME
  --year_min YEAR_MIN   starting value for the years range in the search query
  --year_max YEAR_MAX   ending value for the years range in the search query
  --pos POS [POS ...], --position POS [POS ...]
                        positions for the search query. Defaults to all
                        postions
  --game_num_min GAME_NUM_MIN
  --game_num_max GAME_NUM_MAX
  --week_num_min WEEK_NUM_MIN
  --week_num_max WEEK_NUM_MAX
  --order_by ORDER_BY   What score/points segment the query will be ordered by
```
