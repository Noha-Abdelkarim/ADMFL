# tests/test_trust_engine.py

import unittest

from idt.trust_engine import TrustEngine


class TestTrustEngine(unittest.TestCase):

    def setUp(self):

        self.config = {
            "trust_management": {
                "trust_threshold": 0.5,
                "trust_memory_factor": 0.7
            }
        }

        self.engine = TrustEngine(self.config)

    def test_initialize_uav(self):

        self.engine.initialize_uav("UAV-1")

        self.assertEqual(
            self.engine.get_trust_score("UAV-1"),
            1.0
        )

    def test_compute_trust(self):

        trust_score = self.engine.compute_trust(
            "UAV-1",
            anomaly_score=0.8
        )

        self.assertTrue(
            0.0 <= trust_score <= 1.0
        )

    def test_is_malicious(self):

        self.engine.trust_scores["UAV-1"] = 0.3

        self.assertTrue(
            self.engine.is_malicious("UAV-1")
        )

    def test_reset_trust(self):

        self.engine.trust_scores["UAV-1"] = 0.2

        self.engine.reset_trust("UAV-1")

        self.assertEqual(
            self.engine.get_trust_score("UAV-1"),
            1.0
        )


if __name__ == "__main__":

    unittest.main()