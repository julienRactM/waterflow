from flask import Flask, render_template, request
from script import model_prediction


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    titles = []

    titles = "Estimating the value of your house in the King County area, Washington State"

    if request.method == 'POST':
        sqft_living = request.form.get('sqft_living')
        sqft_living15 = request.form.get('sqft_living15')
        grade = int(request.form.get('grade'))
        zipcode_class = int(request.form.get('zipcode_class'))

        prediction = model_prediction(sqft_living, sqft_living15, grade, zipcode_class)[0][0]
        # predict_proba = model_prediction(sqft_living, sqft_living15, grade, zipcode_class)[1]

        if prediction :
            comment = f"We estimate your home to be worth {prediction}"
        else :
            comment = "There was an error prediction value !"

        return render_template('index.html', titles = titles, prediction=prediction, comment=comment, sqft_living=sqft_living,\
            sqft_living15=sqft_living15, grade=grade, zipcode_class=zipcode_class,) # active_tab='home' predict_proba = np.round(predict_proba[0][1], 2)


    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug = True)
    # app.run(host='0.0.0.0', port=8080)
    # print("app_started1")
    # app.run(debug=True)
    # print("app_started2")
