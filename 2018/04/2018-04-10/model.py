import pandas as pd
import numpy as np
import pickle
import requests
import json
import time
from sklearn.linear_model import LinearRegression


def fetch():
    data = requests.get(
        'http://ec2-54-213-178-139.us-west-2.compute.amazonaws.com:3000/').text
    return json.loads(data)


def write(data):
    # you would actually write this to database
    with open('cars.csv', 'a') as f:
        line = f"{data['mpg']},{data['cylinders']},0,{data['horsepower']},{data['weight']},0,0,0,0\n"
        f.write(line)


def train():
    df = pd.read_csv('cars.csv')
    y = df.mpg
    X = df[['cylinders', 'horsepower', 'weight']]
    model = LinearRegression()
    model.fit(X, y)
    pickle.dump(model, open("linreg.p", "wb"))


def reload():
    requests.get('http://localhost:3333/reload')


if __name__ == '__main__':
    while True:
        time.sleep(5)
        data = fetch()
        write(data)
        train()
        reload()
        print('training:', data)
