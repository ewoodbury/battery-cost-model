# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt
# import pandas as pd

# This function runs the full model and outputs the cost for a single model_id

from model_class import Model
model_0 = Model(0)
print(f"The model_id is {model_0.model_id}")

genParameters = {
    'cellType':'18650',
    'npRatio':1.02,
    'electrodeLength':110, #cm
    'electrodeWidth':5 #cm
    } 

catFormula = {'li':1,'ni':.333,'mn':.333,'co':.333,'al':0,'o':2}
catParameters = {'formula':catFormula,
    'catCapacity': 160, #mAh/g
    'catLoading': 25 #mg/cm2
    }

anParameters = {'anCapacity': 360}

elyteParameters = {'elyte_costPerCell':0.2}

separatorParameters = {'separator_costPerCell':.05}

model_0.get_genParameters(genParameters)

print(f"The N-P Ratio is {model_0.npRatio}")