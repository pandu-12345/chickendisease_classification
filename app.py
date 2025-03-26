from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
import os
from cnnClassifier.pipeline.prediction import Prediction



os.putenv('LANG','en.US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')




app = Flask(__name__)
CORS(app)



class clientapp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = Prediction(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods=['GET','POST'], endpoint="trainendpoint")
@cross_origin()
def training():
    os.system("dvc repro")
    return "Training done succecfully>>>>>>>>"


@app.route("/predict", methods=['POST'],endpoint="predictionendpoint")
@cross_origin()
def prediction():
    img = request.json['image']
    decodeImage(img, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    clApp= clientapp()
    app.run(host='0.0.0.0',port=5000,debug=True)