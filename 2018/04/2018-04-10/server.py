import sys
import pickle
import pandas as pd
from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)
model = None


@app.route('/', methods=['GET'])
def home():
    """
    http --verbose :3333
    open /Applications/Google\ Chrome.app http://localhost:3333
    """
    return "<h1>hello world</h1>"


@app.route('/version', methods=['GET'])
def version():
    """
    http --verbose :3333/version
    """
    return sys.version


@app.route('/square', methods=['POST'])
def square():
    """
    http -b POST :3333/square x:=7
    """
    req = request.get_json()
    x = req['x']
    return jsonify({'input': x, 'output': x**2})


@app.route('/jdemo', methods=['POST'])
def jdemo():
    """
    http --verbose POST :3333/jdemo a=1 b:=2 c:='[2.718,3,"z",true]' d:='{"point":[5,7]}' data:=@sample.json
    http -b POST :3333/jdemo a=1 b:=2 c:='[2.718,3,"z",true]' d:='{"point":[5,7]}' data:=@sample.json
    """
    req = request.get_json()
    fido = req['data']['dogs'][0]
    return jsonify(fido)


@app.route('/about', methods=['GET'])
def about():
    """
    http --verbose :3333/about
    open /Applications/Google\ Chrome.app http://localhost:3333/about
    """
    return render_template('about.html')


@app.route('/faq', methods=['GET'])
def faq():
    """
    http --verbose :3333/faq
    open /Applications/Google\ Chrome.app http://localhost:3333/faq
    """
    return render_template('faq.html')


@app.route('/mpg', methods=['GET'])
def mpg():
    """
    http --verbose :3333/mpg
    open /Applications/Google\ Chrome.app http://localhost:3333/mpg
    """
    return render_template('mpg.html')


@app.route('/inference', methods=['POST'])
def inference():
    """
    called from jquery
    """
    req = request.get_json()
    predictions = model.predict(
        [[req['cylinders'], req['horsepower'], req['weight']]])
    return jsonify(predictions[0])


@app.route('/reload', methods=['GET'])
def reload():
    """
    called from model
    """
    global model
    model = pickle.load(open("gbr.p", "rb"))
    print(model.coef_)
    return 'OK'


@app.route('/d3', methods=['GET'])
def d3():
    """
    called from jquery
    """
    df = pd.read_csv('cars.csv')
    data = list(zip(df.mpg.values.tolist(), df.weight.values.tolist()))
    return jsonify({'data': data})


if __name__ == '__main__':
    reload()
    app.run(host='0.0.0.0', port=3333, debug=True)
