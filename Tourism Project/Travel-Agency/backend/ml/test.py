import pandas as pd
import joblib
import sys
import os

def predict_price(input_data):
    try:
        # Load the trained model
        # Adjust the path to the model as needed depending on where test.py is run from
        model_path = os.path.join(os.path.dirname(__file__), "tourism_price_model.pkl")
        model = joblib.load(model_path)
    except FileNotFoundError:
        print(f"Error: Model file '{model_path}' not found. Please run the training code first.")
        sys.exit(1)

    # Make prediction
    prediction = model.predict(input_data)
    return prediction[0]

if __name__ == "__main__":
    # Example input data matching the format expected by the model
    new_data = pd.DataFrame([{
        "Location": "Goa",
        "Num_Days": 4,
        "Num_People": 2,
        "Food_Level": "Premium",
        "Hotel_Rating": 4,
        "Guide_Support": "Yes",
        "Transport_Type": "Flight",
        "Season": "Peak",
        "Distance_km": 5,
        "Activities_Count": 6
    }])

    print("Testing the model with sample data:")
    print("-" * 30)
    for col in new_data.columns:
        print(f"{col}: {new_data.iloc[0][col]}")
    print("-" * 30)
    
    predicted_price = predict_price(new_data)
    print(f"Predicted Price: {predicted_price:.2f}")
