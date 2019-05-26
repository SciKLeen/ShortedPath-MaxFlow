#from flask import Flask, render_template #, request 
from flask import Flask, render_template, redirect, url_for, request, jsonify
from getLineTest import shortestpath
import json

app = Flask(__name__)
 
# url_for('static', filename='main.css')

# @app.route('/')
# def hello():
#     return render_template('index.html')

# Route for handling the login page logic


# -------------------------------------------------------------------- Main Page -----------------------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def mainpage():
    accept = ""
    origin = ""
    destination = ""
    if request.method == 'POST':
        # lay toa do de tinh toan
        origin = request.form['Origin']
        destination = request.form['Destination']
        if(origin == "" or destination == ""):
            errorOri = ""
            errorDes = ""
            if(origin == ""):
                errorOri = "Origin invalid!"
            if(destination == ""):
                errorDes = "Destination invalid!"
                #print(destination == "")
            return render_template('index.html', origin=origin, destination=destination, errorOri=errorOri, errorDes=errorDes)
        else:
            with open('static/JSON/flows1.json', 'r', encoding='utf8') as json_file:  
                flows = json.load(json_file)

            flow_lst = []
            for item in flows:
                if(item['stated'] == '1'):
                    ls_str = (item['line']).split("-")
                    flow_lst.append(ls_str)
            #chay ham tinh toan
            data = shortestpath(origin, destination, flow_lst)
            #flow = shortestpath(origin, destination, flow_lst)
            
            accept = "True"
            return render_template('index.html', accept=accept, data = json.dumps(data), origin = origin, destination = destination)
    return render_template('index.html', origin = origin, destination = destination)

# --------------------------------------------------------- Admin Page --------------------------------------------------
@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    def loadfile():
        flows = []
        with open('static/JSON/flows1.json', 'r', encoding='utf8') as json_file:  
            flows = json.load(json_file)
        return flows

 
    if request.method == 'POST':
        jsdata = request.form['canvas_data']
        dataFlow = json.loads(jsdata)
        print(dataFlow)
        ##unique_id = create_csv(jsdata)
        ##params = { 'uuid' : unique_id }

        with open('static/JSON/flows1.json', 'w', encoding='utf8') as json_file:  
            json.dump(dataFlow, json_file)

        #with open('static/Json/flows1.txt', 'w') as f:  
        #    f.writelines(jsdata)
        return render_template('admin.html')
    return render_template('admin.html', accept = "True", flows = json.dumps(loadfile()))


if __name__ == '__main__':
    app.run()


