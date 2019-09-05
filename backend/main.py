import pandas as pd
from knn.model import predict
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


knn_df =pd.read_csv('https://raw.githubusercontent.com/mcunha95/CarbonFoodPrint/knn/KNN/formated_normalized_food_per_country_ageGroup.csv')
example_in = knn_df.iloc[70,2:]


@app.route("/api/predict_country")
def knn_predict():
    return jsonify(predict([example_in]))

if __name__ == '__main__':
    app.run(debug=True, port=8888)
