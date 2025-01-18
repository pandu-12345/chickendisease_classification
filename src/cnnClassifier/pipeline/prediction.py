from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
from cnnClassifier.loggs import logger
import numpy as np
import os


class Prediction:
    def __init__(self,filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("artifacts","training","model.keras"))
        image_name=self.filename
        test_image= image.load_img(image_name,target_size=(224,224))
        test_image=image.img_to_array(test_image)
        test_image= np.expand_dims(test_image,axis=0)
        result= np.argmax(model.predict(test_image),axis=1)
        print(result)
        if result[0] == 1 :
            prediction= "Healthy"
            return [{"image" : prediction}]
        else :
            prediction= "Coccidiosis"
            return [{"image" : prediction}]
