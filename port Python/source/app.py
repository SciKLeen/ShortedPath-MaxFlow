#from flask import Flask, render_template #, request 
from flask import Flask, render_template, redirect, url_for, request
from getLine import shortestpath
import json

app = Flask(__name__)
 
# url_for('static', filename='main.css')

@app.route('/')
def hello(name = None):
    return render_template('index.html')


# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def getdirection():
    accept = ""
    if request.method == 'POST':
        # lay toa do de tinh toan
        p1 = request.form['Latitude']
        p2 = request.form['Longtitude']

        #chay ham tinh toan
        data = shortestpath(p1, p2)
        accept = "True"
        with open('static/respon.json', 'w') as outfile:  
            json.dump(data, outfile)
        return render_template('index.html', accept=accept)



if __name__ == '__main__':
    app.run()