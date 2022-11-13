import json
with open("Columns.json", "r") as f:
    col=json.load(f)["columns"]

print(col)

import sklearn
import pickle
with open("model.pkl","rb") as m:
    rid = pickle.load(m)

import numpy as np
import pandas as pd



def predict_price(sqft, bhk, bath, balcony, location):
    input = np.zeros(len(col))
    try:
        loc_index = col.index(location)
    except:
        loc_index = -1
    finally:
        input[0] = sqft
        input[1] = bath
        input[2] = balcony
        input[3] = bhk
        if loc_index >= 0:
            input[loc_index] = 1
    return rid.predict([input])[0][0]

print(predict_price(1000,2,2,1,'HBR Layout'))

