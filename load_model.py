import tensorflow as tf
from tensorflow.keras import models

def model():
    model_cnn = tf.keras.models.load_model('modelob.h5')
    return model_cnn