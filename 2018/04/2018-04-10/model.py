import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import GradientBoostingRegressor

# delete many ? rows
df = pd.read_csv('cars.csv')
y = df.mpg
X = df.drop(['mpg', 'car_name', 'origin'], axis=1)
model = GradientBoostingRegressor(n_estimators=1000)
model.fit(X, y)
pickle.dump(model, open("gbr.p", "wb"))
