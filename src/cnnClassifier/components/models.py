import os
import urllib.request as request
import tensorflow as tf
from  cnnClassifier.loggs import  logger
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig




class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model= tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.Params_image_size,
            include_top=self.config.Params_includetop,
            weights=self.config.Params_weights
        )


        self.save_model(path=self.config.base_model,model=self.model)


    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable= False
        flatten_in=tf.keras.layers.Flatten()(model.output)

        prediction= tf.keras.layers.Dense(
            units= classes,
            activation= "softmax"
        )(flatten_in)

        full_model= tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )
        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.update_base_model=self._prepare_full_model(
            model=self.model,
            classes=self.config.Params_class,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.Params_learning_rate
        )
        self.save_model(path=self.config.update_base_model, model=self.update_base_model)
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

