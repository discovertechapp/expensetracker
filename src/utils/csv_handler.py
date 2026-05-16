import pandas as pd
import os

DATA_DIR = "data"


def read_csv_file(file_name):

    path = os.path.join(DATA_DIR, file_name)

    if not os.path.exists(path):
        return pd.DataFrame()

    return pd.read_csv(path)


def write_csv_file(file_name, dataframe):

    path = os.path.join(DATA_DIR, file_name)

    dataframe.to_csv(path, index=False)
