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

    def test_model_inference(self):
        """Test the model's inference using CSV samples."""
        features = self.data[self.feature_columns].values

        # Perform inference
        predictions = self.model.predict(features)

        # Ensure predictions are valid
        self.assertEqual(len(predictions), len(features))


if __name__ == "__main__":
    unittest.main()