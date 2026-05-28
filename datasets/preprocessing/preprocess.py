# datasets/preprocessing/preprocess.py

import logging
from sklearn.preprocessing import (
    MinMaxScaler
)
from sklearn.impute import SimpleImputer


class DataPreprocessor:

    def __init__(self):

        self.scaler = MinMaxScaler()

        self.imputer = SimpleImputer(
            strategy="mean"
        )

        logging.info(
            "Data Preprocessor initialized."
        )

    def handle_missing_values(
        self,
        dataframe
    ):

        processed_data = self.imputer.fit_transform(
            dataframe
        )

        logging.info(
            "Missing values handled."
        )

        return processed_data

    def normalize_features(
        self,
        dataframe
    ):

        normalized_data = self.scaler.fit_transform(
            dataframe
        )

        logging.info(
            "Features normalized."
        )

        return normalized_data

    def preprocess_pipeline(
        self,
        dataframe
    ):

        processed_data = self.handle_missing_values(
            dataframe
        )

        normalized_data = self.normalize_features(
            processed_data
        )

        logging.info(
            "Preprocessing pipeline completed."
        )

        return normalized_data