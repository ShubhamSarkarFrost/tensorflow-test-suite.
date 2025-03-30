import unittest
import pandas as pd
import tensorflow as tf
import numpy as np
from utils.reporter import TestReportGenerator


class TestModelTraining(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the TensorFlow model and load CSV data."""
        print("\n🔧 Setting up the model and loading CSV data...")

        # Load the CSV file from the /data folder
        cls.data = pd.read_csv('data/sample_data.csv')

        # Create a basic TensorFlow model
        cls.model = tf.keras.Sequential([
            tf.keras.layers.Dense(3, activation='relu', input_dim=3),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        cls.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def test_model_training(self):
        """Train the model and verify the accuracy."""
        features = self.data[['age', 'income', 'credit_score']].values
        labels = self.data['loan_approval'].values

        # Dummy training for testing purposes
        history = self.model.fit(features, labels, epochs=5, batch_size=16, verbose=0)

        accuracy = history.history['accuracy'][-1]

        # Assert that accuracy is reasonable (>50%)
        self.assertGreater(accuracy, 0.5, "Model accuracy is too low")


if __name__ == "__main__":
    unittest.main()
