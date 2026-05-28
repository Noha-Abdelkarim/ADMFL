# visualization/plot_metrics.py

import logging
import matplotlib.pyplot as plt


class MetricsVisualizer:

    def __init__(self):

        logging.info(
            "Metrics Visualizer initialized."
        )

    def plot_bar_chart(
        self,
        labels,
        values,
        title,
        xlabel,
        ylabel
    ):

        plt.figure(figsize=(10, 6))

        plt.bar(labels, values)

        plt.title(title)

        plt.xlabel(xlabel)

        plt.ylabel(ylabel)

        plt.grid(True)

        plt.tight_layout()

        plt.show()

        logging.info(
            f"{title} plotted successfully."
        )

    def plot_accuracy_comparison(
        self,
        models,
        accuracies
    ):

        self.plot_bar_chart(
            labels=models,
            values=accuracies,
            title="Model Accuracy Comparison",
            xlabel="Models",
            ylabel="Accuracy (%)"
        )

    def plot_detection_latency(
        self,
        attack_scenarios,
        latencies
    ):

        self.plot_bar_chart(
            labels=attack_scenarios,
            values=latencies,
            title="Detection Latency Across Attacks",
            xlabel="Attack Scenarios",
            ylabel="Latency (s)"
        )

    def plot_throughput(
        self,
        attack_scenarios,
        throughput_values
    ):

        self.plot_bar_chart(
            labels=attack_scenarios,
            values=throughput_values,
            title="Network Throughput Stability",
            xlabel="Attack Scenarios",
            ylabel="Throughput (%)"
        )

    def save_plot(
        self,
        filename
    ):

        plt.savefig(filename)

        logging.info(
            f"Plot saved as {filename}"
        )