import sys
import pandas as pd
import mlflow
import warnings

def model_prediction(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity):

    warnings.filterwarnings("ignore")
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

def error_message():
    print(""" Needs to enter in command line :
        python script.py ph(float range[0-14]) Hardness(float range[0-100])  Solids(float range[0-1000]) Chloramines(float range[0-10]) Sulfate(float range[0-500]) Conductivity(float range[0-100]) Organic_carbon(float range[0-50]) Trihalomethanes(float range[0-200]) Turbidity(float range[0-10])""")
    return

def main():


    if len(sys.argv) == 10:
        ph = float(sys.argv[1])
        Hardness = float(sys.argv[2])
        Solids = float(sys.argv[3])
        Chloramines = float(sys.argv[4])
        Sulfate = float(sys.argv[5])
        Conductivity = float(sys.argv[6])
        Organic_carbon = float(sys.argv[7])
        Trihalomethanes = float(sys.argv[8])
        Turbidity = float(sys.argv[9])
    else :
        error_message()
        return

    prediction = model_prediction(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity)

    if prediction:
        print("L'eau est potable." if prediction[0] == 1 else "L'eau est non-potable.")
        return "L'eau est potable." if prediction[0] == 1 else "L'eau est non-potable."
    else:
        return print("Invalid prediction")


if __name__ == "__main__":
    main()
