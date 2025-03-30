import unittest
import pandas as pd
import tensorflow as tf
import numpy as np
from utils.reporter import TestReportGenerator


class TestModelPerformance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load CSV data and create model."""
        print("\n🔧 Setting up model for performance tests...")

        # Load CSV from the /data folder
        cls.data = pd.read_csv('data/sample_data.csv')

        # Create a simple TensorFlow model
        cls.model = tf.keras.Sequential([
            tf.keras.layers.Dense(3, activation='relu', input_dim=3),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        cls.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def test_performance(self):
        """Test model performance on CSV data."""
        features = self.data[['age', 'income', 'credit_score']].values
        labels = self.data['loan_approval'].values

        # Measure performance
        _, accuracy = self.model.evaluate(features, labels, verbose=0)

        self.assertGreater(accuracy, 0.5, "Model accuracy is too low")


if __name__ == "__main__":
    unittest.main()
