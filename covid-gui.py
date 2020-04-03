import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
import argparse
import pandas as pd



def read_data(fname):
    return pd.read_csv(fname)


if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)
    print(data)