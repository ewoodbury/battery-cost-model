# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt
# import pandas as pd

# This function runs the full model and outputs the cost for a single model_id

from model_class import Model
from cell_parameters import allParameters
from prices import allPrices


model_0 = Model(0)
print(f"The model_id is {model_0.model_id}.")

model_0.get_allParameters(allParameters)
print(f"The Al foil thickness is {model_0.alFoilThickness} microns.")

model_0.get_allPrices(allPrices)
print(f"The separator price is {model_0.price_separator} USD per 500m roll.")

model_0.calc_allPreliminary()
print(f"The cell energy for Model ID {model_0.model_id} is {model_0.cellEnergy} Wh.")

model_0.calc_allCosts()
print(f"The separator cost is {model_0.cost_separator} per cell.")