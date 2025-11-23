import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plotting import *


def main():
    data = pd.read_csv("data.csv")
    fig, ax = plt.subplots()

    print(data["Crunchiness"] > data["Juiciness"])
    good_apples = data[data["Quality"] == "good"]
    bad_apples = data[data["Quality"] == "bad"]
    pie_chart(ax, [len(good_apples), len(bad_apples)], ["Good", "Bad"])
    plt.show()

    # # 4. Histogram
    histogram(ax, good_apples["Size"], number_of_bins=20)
    set_titles(ax, title="Good Apples", x_label="Size", y_label="Frequency")
    # save_plot(fig, "histogram_good.png")
    # plt.cla()

    histogram(ax, bad_apples["Size"], number_of_bins=20)
    set_titles(ax, title="Bad Apples", x_label="Size", y_label="Frequency")
    save_plot(fig, "histogram.png")
    plt.show()


if __name__ == "__main__":
    main()
