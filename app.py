from flask import Flask, render_template, request
import Model as m
import math
col=m.col[4:]
app = Flask(__name__)
__price = None
@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        sqft=request.form['Squareft']
        bhk=request.form['uiBHK']
        bath=request.form['uiBathrooms']
        balcony=request.form['uiBalcony']
        location=request.form['uiLocations']
        global __price
        result=m.predict_price(sqft, bhk, bath, balcony, location)
        __price = round(result,3)
    return render_template('UI.html', cols=col, Price=__price)

if __name__ == "__main__":
    app.run(debug=True)


