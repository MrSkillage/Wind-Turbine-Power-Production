# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
# tensorflow for keras
import tensorflow.keras as kr
# jsonify from flask to json data
from flask import jsonify

# Create a new web app.
app = fl.Flask(__name__)

# Add default (home) route.
@app.route('/')
def home():
    return app.send_static_file("index.html")


# Create access to the model.h5
@app.route("/api/power/<speed>")
def power(speed):
    theModel = kr.models.load_model("Jupyter_Notebooks\model.h5")
    theSpeed = float(speed)
    powerResult = theModel.predict([theSpeed])
    return jsonify({"value":powerResult.item(0)})

# Add uniform route
@app.route("/api/uniform")
def uniform():
    return {"value" : np.random.normal()}
