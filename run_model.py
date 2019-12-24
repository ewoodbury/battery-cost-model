

# This function runs the full model and outputs the cost for a single model_id

from model_class import Model
# from cell_parameters import allParameters
# from prices import allPrices

import json
with open(r'.\cell_inputs\nmc111.json') as cellInput_json:  
    cellInput = json.load(cellInput_json)
with open(r'.\price_inputs\price_0.json') as priceInput_json:  
    priceInput = json.load(priceInput_json)

model_0 = Model(cellInput,priceInput)

model_0.get_cellParameters()
model_0.get_prices()

print(model_0.elyte)

print(f"The cell_id is {model_0.cellId}.")

print(f"The Al foil thickness is {model_0.alFoilThickness} microns.")

print(f"The separator price is {model_0.price_separator} USD per 500m roll.")

model_0.calc_allPreliminary()
print(f"The cell energy for Cell ID {model_0.cellId} is {model_0.cellEnergy} Wh.")

model_0.calc_allCosts()
print(f"The separator cost is {model_0.cost_separator} per cell.")