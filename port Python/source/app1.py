import subprocess
import json
from flask import request, Flask, render_template

def myCode():
    if request.method == 'POST':
        if request.form['action_button'] == 'MyAction':
		
            # # Get value from mypy.py
			# path = "/path/to/python/file"
			# args = "-a data1 -b data2 -c data3 -d data4"
			# cmd = path + "mypy.py " + args
			
			# # Call command
			# p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			# out, err = p.communicate()

            out = {"Hoang Minh" : 5}
			# out to json
            res = json.dumps(out)
			# print to debug
            json.loads(res)
			
    elif request.method == 'GET':
        return render_template('index.html')


# from flask import Flask, render_template #, request 
app = Flask(__name__)
 
# url_for('static', filename='main.css')

@app.route('/')
def hello(name = None):
    return render_template('json.html')


if __name__ == '__main__':
    app.run()
    