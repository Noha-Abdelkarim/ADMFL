# tests/test_anomaly_detector.py

import unittest

from idt.anomaly_detector import AnomalyDetector


class TestAnomalyDetector(unittest.TestCase):

    def setUp(self):

        self.config = {
            "detection": {
                "anomaly_detection_model":
                "Entropy Detector",

                "packet_entropy_threshold": 0.65
            }
        }

        self.detector = AnomalyDetector(
            self.config
        )

    def test_detect_anomaly(self):

        telemetry = {
            "packet_rate": 2000,
            "latency": 150,
            "entropy": 0.95,
            "trust_score": 0.1
        }

        result = self.detector.detect_anomaly(
            telemetry
        )

        self.assertTrue(
            result["is_anomaly"]
        )


if __name__ == "__main__":

    unittest.main()