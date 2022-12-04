import json
import pickle

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = None


@app.route('/predict')
def home():
    return render_template('app.html')


@app.route('/predict', methods=['POST'])
def predict_home_price():
    print("in home price predict function")
    areaIncome = int(request.form['areaIncome'])
    houseAge = int(request.form['houseAge'])
    noOfRooms = int(request.form['noOfRooms'])
    noOfBedrooms = int(request.form['noOfBedrooms'])

    response = jsonify({
        'estimated_price': get_estimated_price(areaIncome, houseAge, noOfRooms, noOfBedrooms)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


def get_estimated_price(areaIncome, houseAge, noOfRooms, noOfBedrooms):
    return round(model.predict([[areaIncome, houseAge, noOfRooms, noOfBedrooms]])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts")

    global __data_columns

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global model

    model = pickle.load(open("./artifacts/model.pickle", 'rb'))

    print("loading saved artifcats...done")


if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    load_saved_artifacts()
    app.run()
