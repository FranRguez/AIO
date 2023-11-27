import unittest
import os
from src.predict import predict


class PredictionCase(unittest.TestCase):
    def test_prediction(self):
        result = predict((os.path.join('..', 'data', 'test-data-a.csv')))
        self.assertEqual(True, result > 0.5)
        result = predict((os.path.join('..', 'data', 'test-data-b.csv')))
        self.assertEqual(True, result <= 0.5)


if __name__ == '__main__':
    unittest.main()
