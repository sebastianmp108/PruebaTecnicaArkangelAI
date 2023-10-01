import numpy as np

import load_model
import preprocess


def predict(array):
    #   1. call function to pre-process image: it returns image in batch format
    batch_array_img = preprocess.preprocess(array)
    #   2. call function to load model and predict: it returns predicted class
    model = load_model.model()

    prediction = np.argmax(model.predict(batch_array_img))
    label = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happiness', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}
    predict_index = label[prediction]
    return(predict_index)
