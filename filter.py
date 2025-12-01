from typing import Callable
import pandas as pd
from filter import filter_data


PATH_TO_INPUT_FILE = "*.csv"
PATH_TO_OUTPUT_FILE = "*.csv"


def filter_data(data: pd.DataFrame, function: Callable[[pd.DataFrame], pd.Series[bool]]):
    return data[function(data)]


def main():
    data = pd.read_csv(PATH_TO_INPUT_FILE)

    def filter_function(row): return row["Value"] != None

    data = filter_data(data, filter_function)
    data.to_csv(PATH_TO_OUTPUT_FILE, index=False)


def remove_null_rows():
    data = pd.read_csv(PATH_TO_INPUT_FILE)
    data.dropna(inplace=True)
    data.to_csv(PATH_TO_OUTPUT_FILE, index=False)


if __name__ == "__main__":
    # remove_null_rows()
    main()
