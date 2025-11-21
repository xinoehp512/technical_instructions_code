import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plotting import *


def main():
    data = pd.read_csv("data.csv")
    fig, ax = plt.subplots()

    # ----------------------------
    # Generate Example Data
    # ----------------------------
    # Data for bar and line charts
    x = np.arange(5)
    y = np.array([10, 23, 15, 7, 30])

    # Data for pie chart
    sizes = np.array([40, 25, 20, 10, 5])
    labels = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]

    # Data for histogram
    hist_data = np.random.normal(loc=50, scale=10, size=500)

    # Data for scatter plot
    x_scatter = np.random.rand(100)
    y_scatter = 2 * x_scatter + np.random.randn(100) * 0.1  # linear with noise

    # ----------------------------
    # Create Plots
    # ----------------------------

    # 1. Bar Chart
    bar_chart(ax, x, y)
    set_titles(ax, x_label="Category", y_label="Value", title="Bar Chart")
    save_plot(fig, "bar_chart.png")
    plt.cla()

    # 2. Line Chart
    line_chart(ax, x, y)
    set_titles(ax, x_label="Index", y_label="Value", title="Line Chart")
    save_plot(fig, "line_chart.png")
    plt.cla()

    # 3. Pie Chart
    pie_chart(ax, percentages=sizes, labels=labels)
    set_titles(ax, title="Pie Chart")
    save_plot(fig, "pie_chart.png")
    plt.cla()

    # 4. Histogram
    histogram(ax, hist_data, number_of_bins=20)
    set_titles(ax, title="Histogram", x_label="Value", y_label="Frequency")
    save_plot(fig, "histogram.png")
    plt.cla()

    # 5. Scatter Plot
    scatter_plot(ax, x_scatter, y_scatter)
    set_titles(ax, x_label="X Values", y_label="Y Values", title="Scatter Plot")
    save_plot(fig, "scatter_plot.png")
    plt.cla()


if __name__ == "__main__":
    main()
