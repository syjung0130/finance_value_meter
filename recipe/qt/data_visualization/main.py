import sys
import argparse
import pandas as pd
from main_widget import Widget
from main_window import MainWindow

from PyQt5.QtCore import QDateTime, QTimeZone
from PyQt5.QtWidgets import QApplication

'''
python .\qt\data_visualization\main_app.py -f .\qt\data_visualization\all_hour.csv
'''

def transform_date(utc, timezone=None):
    utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QDateTime().fromString(utc, utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date

def read_data(fname):
    # Read the CSV content
    df = pd.read_csv(fname)

    # Remove wrong magnitudes
    df = df.drop(df[df.mag < 0].index)
    magnitudes = df["mag"]

    # My local timezone
    timezone = QTimeZone(b"Euroupe/Berlin")

    # Get timestamp transformed to our timezone
    times = df["time"].apply(lambda x: transform_date(x, timezone))

    return times, magnitudes

if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)

    # Qt Application
    app = QApplication(sys.argv)
    
    widget = Widget(data)
    window = MainWindow(widget)
    window.show()

    print(data)
    sys.exit(app.exec_())