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

        # Automatically detect feature columns and label column
        # Assume the last column is the label
        cls.feature_columns = cls.data.columns[:-1].tolist()
        cls.label_column = cls.data.columns[-1]

        print(f"📊 Detected feature columns: {cls.feature_columns}")
        print(f"🏷️ Detected label column: {cls.label_column}")

        # Determine input shape
        input_shape = (len(cls.feature_columns),)

        # Create a TensorFlow model with dynamic input shape
        cls.model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=input_shape),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        cls.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def test_model_training(self):
        """Train the model and verify the accuracy."""
        features = self.data[self.feature_columns].values
        labels = self.data[self.label_column].values

        # Dummy training for testing purposes
        history = self.model.fit(features, labels, epochs=5, batch_size=16, verbose=0)

        accuracy = history.history['accuracy'][-1]

        # Assert that accuracy is reasonable (>50%)
        self.assertGreater(accuracy, 0.5, "Model accuracy is too low")


if __name__ == "__main__":
    unittest.main()