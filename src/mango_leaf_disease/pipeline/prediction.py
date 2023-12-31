
import numpy as np
import tensorflow as tf
import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename

    
    def predict(self):
        # load model
        model = load_model(os.path.join("final_model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 0:
            prediction = 'Anthracnose: Disease'
            return [{ "image" : prediction}]
        elif result[0] == 1:
            prediction = 'Bacterial Canker: Disease'
            return [{ "image" : prediction}]
        elif result[0] == 2:
            prediction = 'Cutting Weevil: Disease'
            return [{ "image" : prediction}]
        elif result[0] == 3:
            prediction = 'Die Back: Disease'
            return [{ "image" : prediction}]
        elif result[0] == 4:
            prediction = 'Gall Midge: Disease'
            return [{ "image" : prediction}]
        elif result[0] == 6:
            prediction = 'Powdery Mildew: Disease'
            return [{ "image" : prediction}]
        elif result[0] == 7:
            prediction = 'Scooty Mould: Disease'
            return [{ "image" : prediction}]
        else:
            prediction = 'Healthy: Healthy'
            return [{ "image" : prediction}]