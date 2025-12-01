import pandas as pd
import matplotlib.pyplot as plt

from plotting import *


def example():
    data = pd.read_csv("apple_quality.csv")

    # Data Filtering
    good_apples = filter_data(data, lambda row: row["Quality"] == "good")
    bad_apples = filter_data(data, lambda row: row["Quality"] == "bad")

    acid_apples = filter_data(data, lambda row: row["Acidity"] <= 0)
    alkaline_apples = filter_data(data, lambda row: row["Acidity"] > 0)

    # Bar Chart
    fig, ax = plt.subplots()
    bar_chart(ax, x_values=["Acid Apples", "Alkaline Apples"], y_values=[len(acid_apples), len(alkaline_apples)])
    save_plot(fig, "barchart.png")
    plt.show()

    # Pie Chart
    fig, ax = plt.subplots()
    pie_chart(ax, percentages=[len(good_apples), len(bad_apples)], labels=["Good", "Bad"])
    save_plot(fig, "piechart.png")
    plt.show()

    # Histogram
    fig, ax = plt.subplots()
    histogram(ax, x_values=good_apples["Size"], number_of_bins=20)
    histogram(ax, x_values=bad_apples["Size"], number_of_bins=20)
    set_titles(ax, title="Good vs. Bad Apples", x_label="Size", y_label="Frequency")
    save_plot(fig, "histogram.png")
    plt.show()

    # Scatter Plot
    fig, ax = plt.subplots()
    scatter_plot(ax, x_values=data["Juiciness"], y_values=data["Acidity"])
    set_titles(ax, title="Acidity vs Juiciness", x_label="Juciness", y_label="Acidity")
    save_plot(fig, "scatterplot.png")
    plt.show()


def filter_data(data, function):
    return data[function(data)]


if __name__ == "__main__":
    example()
