from flask import Flask,render_template
from flask import request
import rankPredictor as rp

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    name="Arjun Kumar Soni"
    return render_template('index.html',name=name)

@app.route("/features", methods=['GET', 'POST'])

def hello_world2():
    if request.method == 'POST':
        institute=[]
        x=int(request.form['rank'])
        name=rp.predict(x)
        for j in name:
            j=j.to_dict()
            n = 0
            for i in j["S.NO"].values():
                n = i
            institute.append({"name": (j["INSTITUTE NAME"][n]),
                    "branch": (j["BRANCH"][n]),
                    "type":j["INSTITUTE TYPE"][n],
                    "open":j["JEE OPENING RANK"][n],
                    "close":j["JEE CLOSING RANK"][n],
                    "category":j["ALLOTTED CATEGORY"][n]
                    })
        return render_template('predictor.html',institute=institute)
    else:
        return render_template('index1.html')

@app.route("/about", methods=['GET', 'POST'])
def hello_world3():
    name="Arjun Kumar Soni"
    return "about"


app.run(debug=False,host='0.0.0.0')