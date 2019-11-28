import csv
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter


def get_csv_data(filename):
    rows = []
    data_file = open(filename, "r")
    reader = csv.reader(data_file)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows


def get_excel_data(excel_file):
    df = pd.read_excel(excel_file)
    list_mail1 = df["mail1"]
    list_mail2 = df["mail2"]
    excel_data_in_tuple = list(zip(list_mail1, list_mail2))
    return excel_data_in_tuple
