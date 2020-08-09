import argparse
import pandas as pd

# all_hour.csv
# https://statkclee.github.io/sw4ds/sw4ds-earthquake-make-report.html
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv

def read_data(fname):
    return pd.read_csv(fname)


if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)
    print(data)
