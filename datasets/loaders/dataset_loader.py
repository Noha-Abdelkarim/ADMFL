# datasets/loaders/dataset_loader.py

import logging
import pandas as pd


class DatasetLoader:

    def __init__(self):

        logging.info(
            "Dataset Loader initialized."
        )

    def load_csv(
        self,
        file_path
    ):

        logging.info(
            f"Loading dataset: {file_path}"
        )

        dataframe = pd.read_csv(file_path)

        logging.info(
            f"Dataset shape: {dataframe.shape}"
        )

        return dataframe

    def get_dataset_info(
        self,
        dataframe
    ):

        info = {
            "rows": dataframe.shape[0],
            "columns": dataframe.shape[1],
            "features": list(dataframe.columns)
        }

        logging.info(
            "Dataset information extracted."
        )

        return info

    def split_features_labels(
        self,
        dataframe,
        label_column
    ):

        X = dataframe.drop(
            columns=[label_column]
        )

        y = dataframe[label_column]

        logging.info(
            "Features and labels separated."
        )

        return X, y