import pickle
import numpy as np

def load_model():
    with open('hdp_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model
