import joblib
import pandas as pd

# Path to the pre-trained machine learning model
MODEL_PATH = "models/predict_freight_model.pkl"


def load_model(model_path: str = MODEL_PATH):
    """
    Load trained freight cost prediction model.
    """
    model = joblib.load(model_path)
    return model


def predict_freight_cost(input_data):
    """
    Predict freight cost for new vendor invoices.

    Parameters
    ----------
    input_data : dict

    Returns
    -------
    pd.DataFrame
        Input data with predicted freight cost.
    """

    model = load_model()

    input_df = pd.DataFrame(input_data)

    input_df["predicted_Freight"] = (
        model.predict(input_df).round()
    )

    return input_df


if __name__ == "__main__":

    sample_data = {
        "Dollars": [18500, 9000, 3000, 200]
    }

    prediction = predict_freight_cost(sample_data)

    print(prediction)