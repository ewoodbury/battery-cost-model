# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt
# import pandas as pd

# This function runs the full model and outputs the cost for a single model_id

from model_class import Model
model_0 = Model(0)
print(f"The model_id is {model_0.model_id}")

genParameters = {'cellType':'18650', 'npRatio':1.02, 'electrodeLength':50}

model_0.get_genParameters(genParameters)

print(f"The N-P Ratio is {model_0.npRatio}")