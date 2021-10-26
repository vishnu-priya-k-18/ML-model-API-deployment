from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__,template_folder='templates')

@app.route('/',methods = ['GET','POST'])
def getResult():
    result = 0
    if request.method == 'POST':
        model = pickle.load(open('model.pkl', 'rb'))#load
        user_input = request.form.get("experience")# input

        result = model.predict([[user_input]])#predict
        print(result)

    return  render_template("index.html", prediction = result)

if __name__ == "__main__":
    app.run(debug=True, port= 8080)
