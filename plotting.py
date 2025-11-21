from matplotlib.axes import Axes
import matplotlib.pyplot as plt


def bar_chart(ax: Axes, x_values, y_values):
    ax.bar(x=x_values, height=y_values)


def set_titles(ax: Axes, x_label, y_label, title):
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
