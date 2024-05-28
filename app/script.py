import sys
import pandas as pd
import mlflow

def model_prediction(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity):

    mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
    loaded_model = mlflow.pyfunc.load_model('mlflow-artifacts:/892102606047290498/96769e9236bb446aa8a9bd8ae214700d/artifacts/waterflow_model')

    # with open('app/app_model/best_rf_model.pkl', 'rb') as f:
    #     model = pickle.load(f)

    X_test = pd.DataFrame({
        'ph': [ph],
        'Hardness': [Hardness],
        'Solids': [Solids],
        'Chloramines': [Chloramines],
        'Sulfate': [Sulfate],
        'Conductivity': [Conductivity],
        'Organic_carbon': [Organic_carbon],
        'Trihalomethanes': [Trihalomethanes],
        'Turbidity': [Turbidity]
})

    predictions = loaded_model.predict(X_test)
    return [predictions]


if __name__ == "__main__":
    # Example values for testing the function
    ph = 7.0
    Hardness = 150.0
    Solids = 20000.0
    Chloramines = 7.0
    Sulfate = 250.0
    Conductivity = 500.0
    Organic_carbon = 10.0
    Trihalomethanes = 80.0
    Turbidity = 4.0

    # pred non potable

    # ph = 700.0
    # Hardness = 150.0
    # Solids = 200000.0
    # Chloramines = 7.0
    # Sulfate = 250.0
    # Conductivity = 500.0
    # Organic_carbon = 100.0
    # Trihalomethanes = 80.0
    # Turbidity = 4.0

    # Call the function with example values
    result = model_prediction(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity)
    print(result[0])
    print(result[0])
    print(result[0])
    print(result[0])
    print(result[0])
    print(result[0])
    print(result[0])
    print(result[0])
