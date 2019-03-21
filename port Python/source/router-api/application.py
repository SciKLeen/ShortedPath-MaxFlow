from flask import Flask, render_template
app = Flask(__name__)
 
# url_for('static', filename='main.css')
@app.route('/')
def hello(name = None):
    return render_template('index.html')

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
 
if __name__ == '__main__':
    app.run()