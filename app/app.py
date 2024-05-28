from flask import Flask, render_template, request
from script import model_prediction


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    titles = []

    titles = "Estimation du caractère potable de l'eau à partir de relevés"

    if request.method == 'POST':

# ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity
        ph = float(request.form.get('ph'))
        Hardness = float(request.form.get('Hardness'))
        Solids = float(request.form.get('Solids'))
        Chloramines = float(request.form.get('Chloramines'))
        Sulfate = float(request.form.get('Sulfate'))
        Conductivity = float(request.form.get('Conductivity'))
        Organic_carbon = float(request.form.get('Organic_carbon'))
        Trihalomethanes = float(request.form.get('Trihalomethanes'))
        Turbidity = float(request.form.get('Turbidity'))

        print(model_prediction(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity))
        prediction = model_prediction(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity)
        # predict_proba = model_prediction(sqft_living, sqft_living15, grade, zipcode_class)[1]

        # if prediction :
        #     comment = "L'eau est potable." if prediction[0] == 1 else "L'eau est non-potable."
        #     print(comment)

        # else :

        if prediction:
            if prediction[0] == 1:
                comment = "L'eau est potable."
            else:
                comment = "L'eau est non-potable."
            print(comment)
        else :
            comment = "There was an error prediction value !"
        # active_tab='home' predict_proba = np.round(predict_proba[0][1], 2)

        return render_template('index.html', titles=titles, prediction=prediction, comment=comment, ph=ph, Hardness=Hardness,\
            Solids=Solids, Chloramines=Chloramines, Sulfate=Sulfate, Conductivity=Conductivity, Organic_carbon=Organic_carbon,
            Trihalomethanes=Trihalomethanes, Turbidity=Turbidity)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug = True)
    # app.run(host='0.0.0.0', port=8080)
    # print("app_started1")
    # app.run(debug=True)
    # print("app_started2")
