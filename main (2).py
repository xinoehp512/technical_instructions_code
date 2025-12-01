import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plotting import *

# Place your plots in main, then run this file.
# Images will appear in the "images" folder.

DATA_FILE_NAME = "Student Mental health.csv"  # Change this to the name of your data file.

# Comment out visuals that you don't want.
DATA_VISUAL_TYPES = [
    "Bar Chart",
    "Pie Chart",
    "Histogram",
    "Scatter Plot",
]
column = "Quality"


def filter_data(data, function):
    return data[function(data)]


def main():
    data = pd.read_csv(DATA_FILE_NAME)
    print(data)

    # Data Filtering
    good_apples = filter_data(data, lambda row: row[column] == "good")
    bad_apples = filter_data(data, lambda row: row[column] == "bad")

    acid_apples = filter_data(data, lambda row: row["Acidity"] <= 0)
    alkaline_apples = filter_data(data, lambda row: row["Acidity"] > 0)

    # Bar Chart
    if "Bar Chart" in DATA_VISUAL_TYPES:
        fig, ax = plt.subplots()
        bar_chart(ax, x_values=["Acid Apples", "Alkaline Apples"], y_values=[len(acid_apples), len(alkaline_apples)])
        save_plot(fig, "barchart.png")
        plt.show()

    # Pie Chart
    if "Pie Chart" in DATA_VISUAL_TYPES:
        fig, ax = plt.subplots()
        pie_chart(ax, [len(good_apples), len(bad_apples)], ["Good", "Bad"])
        save_plot(fig, "piechart.png")
        plt.show()

    # Histogram
    if "Histogram" in DATA_VISUAL_TYPES:
        fig, ax = plt.subplots()
        histogram(ax, good_apples["Size"], number_of_bins=20)
        histogram(ax, bad_apples["Size"], number_of_bins=20)
        set_titles(ax, title="Good vs. Bad Apples", x_label="Size", y_label="Frequency")
        save_plot(fig, "histogram.png")
        plt.show()

    # Scatter Plot
    if "Scatter Plot" in DATA_VISUAL_TYPES:
        fig, ax = plt.subplots()
        scatter_plot(ax, x_values=data["Juiciness"], y_values=data["Acidity"])
        set_titles(ax, title="Acidity vs Juiciness", x_label="Juciness", y_label="Acidity")
        save_plot(fig, "scatterplot.png")
        plt.show()


if __name__ == "__main__":
    main()
