from pathlib import Path
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def bar_chart(ax: Axes, x_values, y_values):
    ax.bar(x=x_values, height=y_values)


def line_chart(ax: Axes, x_values, y_values):
    ax.plot(x_values, y_values)


def pie_chart(ax: Axes,  percentages, labels=None):
    ax.pie(percentages, labels=labels, autopct="%1.1f%%")


def histogram(ax: Axes, x_values, number_of_bins):
    ax.hist(x_values, bins=number_of_bins)


def scatter_plot(ax: Axes, x_values, y_values):
    ax.scatter(x_values, y_values)


def set_titles(ax: Axes, x_label="", y_label="", title=""):
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


def save_plot(fig: Figure, filename):
    folder_path = Path("images")
    folder_path.mkdir(exist_ok=True)
    fig.savefig(f"images/{filename}")
