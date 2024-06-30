from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from joblib import load
from predict.model import LSTMModel
from predict.predicte import predictPost
import torch

predict_bp = Blueprint("predict", __name__)


@predict_bp.post("/predict_34")
# @jwt_required()
def predict_34_classes():
    scaler = load("static/scaler.joblib")
    # Load the saved model
    model = LSTMModel(1, 64, 2, 34)
    model.load_state_dict(torch.load('assets/lstm_model_34.pth'))
    model.eval()
    result, prob = predictPost(request.json.get('data'), scaler, model, "34")
    return (
        jsonify(
            {
                "Predicted class": result,
                "probability": prob,
            }
        ),
        200,
    )


@predict_bp.post("/predict_8")
# @jwt_required()
def predict_8_classes():
    scaler = load("static/scaler.joblib")
    # Load the saved model
    model = LSTMModel(1, 64, 2, 8)
    model.load_state_dict(torch.load('assets/lstm_model_8.pth'))
    model.eval()
    result, prob = predictPost(request.json.get('data'), scaler, model, "8")
    return (
        jsonify(
            {
                "Predicted class": result,
                "probability": prob,
            }
        ),
        200,
    )


@predict_bp.post("/predict_2")
# @jwt_required()
def predict_2_classes():
    scaler = load("static/scaler.joblib")
    # Load the saved model
    model = LSTMModel(1, 64, 2, 2)
    model.load_state_dict(torch.load('assets/lstm_model_2.pth'))
    model.eval()
    result, prob = predictPost(request.json.get('data'), scaler, model, "2")
    return (
        jsonify(
            {
                "Predicted class": result,
                "probability": prob,
            }
        ),
        200,
    )
