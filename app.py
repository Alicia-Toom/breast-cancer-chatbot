from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/questions")
def api_questions():
    return {
        "area_mean": "What is the area_mean ?",
        "area_se": "What is the area_se ?",
        "area_worst": "What is the area_worst ?",
        "compactness_worst": "What is the compactness_worst ?",
        "concave_points_mean": "What is the concave_points_mean ?",
        "concave_points_worst": "What is the concave_points_worst ?",
        "concavity_mean": "What is the concavity_mean ?",
        "concavity_worst": "What is concavity_worst ?",
        "perimeter_mean": "What is the perimeter_mean ?",
        "perimeter_worst": "What is the perimeter_worst ?",
        "radius_mean": "What is the radius_mean ?",
        "radius_se": "What is the radius_se ?",
        "radius_worst": "What is the radius_worst ?",
        "texture_worst": "What is the texture_worst ?"
    }


@app.route("/api/predict", methods=["POST"])
def api_predict():
    score = predict(area_mean=request.json["area_mean"],
                    area_se=request.json["area_se"],
                    area_worst=request.json["area_worst"],
                    compactness_worst=request.json["compactness_worst"],
                    concave_points_mean=request.json["concave_points_mean"],
                    concave_points_worst=request.json["concave_points_worst"],
                    concavity_mean=request.json["concavity_mean"],
                    concavity_worst=request.json["concavity_worst"],
                    perimeter_mean=request.json["perimeter_mean"],
                    perimeter_worst=request.json["perimeter_worst"],
                    radius_mean=request.json["radius_mean"],
                    radius_se=request.json["radius_se"],
                    radius_worst=request.json["radius_worst"],
                    texture_worst=request.json["texture_worst"])

    return {
        "score": int(score)
    }


@app.route("/debug")
def debug():
    score = predict(area_mean=1001,
                    area_se=153.4,
                    area_worst=2019,
                    compactness_worst=0.6656,
                    concave_points_mean=0.1471,
                    concave_points_worst=0.2654,
                    concavity_mean=0.3001,
                    concavity_worst=0.7119,
                    perimeter_mean=122.8,
                    perimeter_worst=184.6,
                    radius_mean=17.99,
                    radius_se=1.095,
                    radius_worst=25.38,
                    texture_worst=17.33)

    print(f"Got score: {score}")


def predict(radius_mean=None, radius_se=None, radius_worst=None, perimeter_mean=None, perimeter_worst=None,
            area_mean=None, area_se=None, area_worst=None, concavity_mean=None, concavity_worst=None,
            concave_points_mean=None, concave_points_worst=None, compactness_worst=None, texture_worst=None):

    model = pickle.load(open("model_svm.pickle", "rb"))
    result = model.predict([[radius_mean, perimeter_mean, area_mean, concavity_mean, concave_points_mean, radius_se,
                             area_se, radius_worst, texture_worst, perimeter_worst, area_worst, compactness_worst,
                             concavity_worst, concave_points_worst]])

    return result[0]

