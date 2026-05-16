import pandas as pd
import os

DATA_FOLDER = "data"


def get_file_path(file_name):

    return os.path.join(DATA_FOLDER, file_name)


def read_csv_data(file_name):

    file_path = get_file_path(file_name)

    if not os.path.exists(file_path):
        return pd.DataFrame()

    return pd.read_csv(file_path)


def write_csv_data(file_name, dataframe):

    file_path = get_file_path(file_name)

    dataframe.to_csv(
        file_path,
        index=False
    )
