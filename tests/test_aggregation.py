# tests/test_aggregation.py

import unittest

from tafl.aggregation import AggregationManager


class TestAggregation(unittest.TestCase):

    def setUp(self):

        self.aggregator = AggregationManager()

    def test_fedavg_aggregation(self):

        updates = [
            [1.0, 2.0, 3.0],
            [2.0, 3.0, 4.0],
            [3.0, 4.0, 5.0]
        ]

        result = self.aggregator.aggregate(
            updates
        )

        self.assertEqual(
            len(result),
            3
        )

    def test_weighted_aggregation(self):

        updates = [
            [1.0, 2.0],
            [3.0, 4.0]
        ]

        weights = [0.7, 0.3]

        result = self.aggregator.weighted_aggregate(
            updates,
            weights
        )

        self.assertEqual(
            len(result),
            2
        )


if __name__ == "__main__":

    unittest.main()