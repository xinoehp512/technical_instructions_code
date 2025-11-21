import kagglehub
import numpy as np
import os
download_path = os.path.join(os.getcwd(), 'kaggle_downloads')
os.environ['KAGGLEHUB_CACHE'] = download_path


def main():
    path = kagglehub.dataset_download("nelgiriyewithana/apple-quality") + r"\apple_quality.csv"
    data = np.genfromtxt(path, delimiter=",", encoding='ISO-8859-1', dtype=None, names=True)
    data = data[:-1]
    # headers = data.dtype.names
    # print(headers)
    np.save('apple_data', data)


if __name__ == "__main__":
    main()
