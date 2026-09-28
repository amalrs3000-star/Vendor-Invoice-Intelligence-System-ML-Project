import joblib
import pandas as pd


MODEL_PATH = "invoice_flagging/models/predict_flag_invoice.pkl"
SCALER_PATH = "invoice_flagging/models/scaler.pkl"


def load_model(model_path: str = MODEL_PATH):
    """
    Load the trained invoice flagging model.
    """
    model = joblib.load(model_path)
    return model


def load_scaler(scaler_path: str = SCALER_PATH):
    """
    Load the scaler used during model training.
    """
    scaler = joblib.load(scaler_path)
    return scaler


def predict_invoice_flag(input_data):
    """
    Predict whether a vendor invoice should be flagged.
    """

    model = load_model()
    scaler = load_scaler()

    input_df = pd.DataFrame(input_data)

    features = [
        "invoice_quantity",
        "invoice_dollars",
        "Freight",
        "total_item_quantity",
        "total_item_dollars"
    ]

    X = input_df[features]

    X_scaled = scaler.transform(X)

    input_df["Predicted_Flag"] = model.predict(X_scaled)

    return input_df


if __name__ == "__main__":

    sample_data = {
        "invoice_quantity": [50],
        "invoice_dollars": [352.95],
        "Freight": [1.73],
        "total_item_quantity": [162],
        "total_item_dollars": [2476.0]
    }

    prediction = predict_invoice_flag(sample_data)

    print(prediction)