# This function runs the full model and outputs the cost for a 
# single model_id

from cost_model_class import CostModel

import json
with open(r'.\cell_inputs\nmc111.json') as cellInput_json:
    cellInput = json.load(cellInput_json)
with open(r'.\price_inputs\price_0.json') as priceInput_json:
    priceInput = json.load(priceInput_json)

model_0 = CostModel(cellInput, priceInput)
# model_0.get_cellParameters()
# model_0.get_prices()

# model_0.calc_allPreliminary()
# model_0.calc_allCosts()

# print(f"The cell_id is {model_0.cellId}.")
# print(f"The Al foil thickness is {model_0.alFoilThickness} microns.")
# print(f"The separator price is {model_0.price_separator} USD per 500m roll.")
# print(f"The cell energy for Cell ID {model_0.cellId} is {model_0.cellEnergy} Wh.")
# print(f"The separator cost is {model_0.cost_separator} per cell.")

# from plot_model import plot_model
# plot_model(model_0)

# Plotting: (super basic)
costDict_cellBasis = model_0.return_allCosts_cellBasis()
costDict_kwhBasis = model_0.return_allCosts_kwhBasis()
print(costDict_kwhBasis)

import matplotlib.pyplot as plt
plt.figure()
plt.pie(costDict_kwhBasis.values(), labels=costDict_kwhBasis.keys())
plt.tight_layout()
plt.show()
