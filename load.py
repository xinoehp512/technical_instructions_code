import kagglehub
import pandas as pd
import os
download_path = os.path.join(os.getcwd(), 'kaggle_downloads')
os.environ['KAGGLEHUB_CACHE'] = download_path


def main():
    path = kagglehub.dataset_download("nelgiriyewithana/apple-quality") + r"\apple_quality.csv"
    data = pd.read_csv(path)
    data.dropna(inplace=True)
    data.to_csv("data.csv", index=False)


if __name__ == "__main__":
    main()
