# evaluation/metrics.py

import logging

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


class EvaluationMetrics:

    def __init__(self):

        logging.info(
            "Evaluation Metrics module initialized."
        )

    def compute_accuracy(
        self,
        y_true,
        y_pred
    ):

        accuracy = accuracy_score(
            y_true,
            y_pred
        )

        logging.info(
            f"Accuracy: {accuracy:.4f}"
        )

        return accuracy

    def compute_precision(
        self,
        y_true,
        y_pred
    ):

        precision = precision_score(
            y_true,
            y_pred,
            average="weighted"
        )

        logging.info(
            f"Precision: {precision:.4f}"
        )

        return precision

    def compute_recall(
        self,
        y_true,
        y_pred
    ):

        recall = recall_score(
            y_true,
            y_pred,
            average="weighted"
        )

        logging.info(
            f"Recall: {recall:.4f}"
        )

        return recall

    def compute_f1_score(
        self,
        y_true,
        y_pred
    ):

        f1 = f1_score(
            y_true,
            y_pred,
            average="weighted"
        )

        logging.info(
            f"F1-Score: {f1:.4f}"
        )

        return f1

    def compute_confusion_matrix(
        self,
        y_true,
        y_pred
    ):

        matrix = confusion_matrix(
            y_true,
            y_pred
        )

        logging.info(
            "Confusion Matrix computed."
        )

        return matrix

    def evaluate_all_metrics(
        self,
        y_true,
        y_pred
    ):

        results = {
            "accuracy": self.compute_accuracy(
                y_true,
                y_pred
            ),

            "precision": self.compute_precision(
                y_true,
                y_pred
            ),

            "recall": self.compute_recall(
                y_true,
                y_pred
            ),

            "f1_score": self.compute_f1_score(
                y_true,
                y_pred
            ),

            "confusion_matrix": self.compute_confusion_matrix(
                y_true,
                y_pred
            )
        }

        logging.info(
            "All evaluation metrics computed."
        )

        return results