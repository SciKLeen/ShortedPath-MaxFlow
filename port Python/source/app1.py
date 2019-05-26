#from flask import Flask, render_template #, request 
from flask import Flask, render_template, redirect, url_for, request, jsonify
from getLine import shortestpath
import json

app = Flask(__name__)
 
# url_for('static', filename='main.css')

temp = "hoang"
# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def getdirection():
    if request.method == 'POST':
        Items = [
                {
                "name": "John",
                "lastname": "Smith", 
                "age": 22, 
                },
                {
                "name": "123",
                "lastname": "Smith", 
                "age": 22, 
                }
        ]
        return render_template("index1.html", items=json.dumps(Items), varial = "123456")
    return render_template('index1.html')


if __name__ == '__main__':
    app.run()