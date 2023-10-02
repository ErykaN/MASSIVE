import os
import tarfile
import pandas as pd

def extract_tar_file(tar_file, output_dir):
    with tarfile.open(tar_file, 'r:gz') as tar:
        tar.extractall(path=output_dir)

def load_dataset(file_path):
    try:
        # Load the dataset using pandas
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Dataset file not found.")
        return None
    except pd.errors.EmptyDataError:
        print("The dataset file is empty or has no columns to parse.")
        return None

if __name__ == "__main__":
    # Path to the .tar file
    tar_file_path = "C:/Users/User/Documents/data/amazon.gz"

    # Extract the .tar file
    extract_tar_file(tar_file_path, "C:/Users/User/Desktop/MASSIVE/data/amazon_massive_dataset")
