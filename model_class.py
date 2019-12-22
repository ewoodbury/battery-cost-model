class Model:

    #Initializer:
    def __init__(self, model_id):
        self.model_id = model_id

    #Now: define method to extract general parameters from each parameter dictionary
    def get_genParameters(self, genParameters):
        self.cellType = genParameters['cellType']
        self.npRatio = genParameters['npRatio']
        self.electrodeLength = genParameters['electrodeLength']