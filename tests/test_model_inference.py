import unittest
import pandas as pd
import tensorflow as tf
import numpy as np
from utils.reporter import TestReportGenerator


class TestModelInference(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load CSV data and set up model."""
        print("\n🔧 Setting up the model for inference...")

        # Load the CSV file from /data folder
        cls.data = pd.read_csv('data/sample_data.csv')

        # Create a basic TensorFlow model
        cls.model = tf.keras.Sequential([
            tf.keras.layers.Dense(3, activation='relu', input_dim=3),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        cls.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def test_model_inference(self):
        """Test the model's inference using CSV samples."""
        features = self.data[['age', 'income', 'credit_score']].values

        # Perform inference
        predictions = self.model.predict(features)

        # Ensure predictions are valid
        self.assertEqual(len(predictions), len(features))


if __name__ == "__main__":
    unittest.main()
