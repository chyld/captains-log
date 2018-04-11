import sys
import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

model = pickle.load(open("gbr.p", "rb"))


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, debug=True)
