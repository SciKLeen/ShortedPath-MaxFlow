from flask import Flask, render_template
app = Flask(__name__)
 
# url_for('static', filename='main.css')

@app.route('/')
def hello(name = None):
    return render_template('index1.html')


if __name__ == '__main__':
    app.run()