import pandas as pd
import matplotlib.pyplot as plt

from filter import filter_data
from plotting import *

# Place your plots in main, then run this file.
# Images will appear in the "images" folder.

DATA_FILE_NAME = "*.csv"  # Change this to the name of your data file.
PLOT_FILE_NAME = "*.png"  # Change this to the name you want your ouput image to have.


def main():
    data = pd.read_csv(DATA_FILE_NAME)
    fig, ax = plt.subplots()

    # Put the code to draw your graph here.

    save_plot(fig, PLOT_FILE_NAME)
    plt.show()


if __name__ == "__main__":
    main()
