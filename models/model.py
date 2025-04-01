import tensorflow as tf


def create_model(input_shape):
    """
    Create a model with the specified input shape.

    Args:
        input_shape (tuple): Shape of the input features

    Returns:
        tf.keras.Model: A compiled TensorFlow model
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=input_shape),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model