import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd


from model_class import Model

def plot_model(model):
    '''Creates a simple plot of the cost breakdown from a Model instance. 

    Note that the instance must have had its calculate methods
    executed already so that the cost results are present.
    '''
    assert isinstance(model, Model),"Input must be an instance of class Model!"

    costDict = model.return_allCosts()
    print(costDict)

    print("hello")
    plt.figure()
    plt.pie(costDict.values(), labels = costDict.keys())
    plt.show()

