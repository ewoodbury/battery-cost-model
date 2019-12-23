# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt
# import pandas as pd

# This function runs the full model and outputs the cost for a single model_id

from model_class import Model
from cell_parameters import allParameters


model_0 = Model(0)
print(f"The model_id is {model_0.model_id}")

model_0.get_allParameters(allParameters)
print(f"The Can cost is ${model_0.canCostPerCell} per cell")