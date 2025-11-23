import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plotting import *


DATA_FILE_NAME = "apple_quality.csv"  # Change this to the name of your data file.


def filter_data(data, function):
    return data[function(data)]


def main():
    data = pd.read_csv(DATA_FILE_NAME)
    fig, ax = plt.subplots()

    # Data Filtering
    good_apples = data[data["Quality"] == "good"]
    bad_apples = data[data["Quality"] == "bad"]

    def filter_good(row):
        return row["Quality"] == "good"

    def filter_bad(row):
        return row["Quality"] == "bad"
    good_apples = filter_data(data, filter_good)
    bad_apples = filter_data(data, filter_bad)

    # good_apples = filter_data(data, lambda row: row["Quality"] == "good")

    def get_acid(row):
        return row["Acidity"]

    # Pie Chart
    print(data["Crunchiness"] > data["Juiciness"])
    pie_chart(ax, [len(good_apples), len(bad_apples)], ["Good", "Bad"])
    # save_plot(fig, "piechart.png")
    plt.show()
#
    fig, ax = plt.subplots()

    # Histogram
    histogram(ax, good_apples["Size"], number_of_bins=20)
    histogram(ax, bad_apples["Size"], number_of_bins=20)
    set_titles(ax, title="Good vs. Bad Apples", x_label="Size", y_label="Frequency")
    save_plot(fig, "histogram.png")
    plt.show()


if __name__ == "__main__":
    main()
