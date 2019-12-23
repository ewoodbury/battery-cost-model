from my_functions import get_molar_mass

class Model:

    #Initializer:
    def __init__(self, model_id):
        self.model_id = model_id

    #Now: define method to extract input parameters from input dictionaries
    def get_genParameters(self, genParameters):
        self.cellType = genParameters['cellType']
        self.npRatio = genParameters['npRatio']
        self.electrodeLength = genParameters['electrodeLength'] #cm
        self.electrodeWidth = genParameters['electrodeWidth'] #cm
        self.electrodeOneSidedArea = self.electrodeLength*self.electrodeWidth #cm
        
    def get_catParameters(self, catParameters):
        self.catFormula = catParameters['catFormula']
        self.catCapacity = catParameters['catCapacity']
        self.catLoading = catParameters['catLoading']
        self.catActiveFrac = catParameters['catActiveFrac']
        self.catBinderFrac = catParameters['catBinderFrac']
        self.catConductorFrac = catParameters['catConductorFrac']
    
    def get_anParameters(self, anParameters):
        self.anCapacity = anParameters['anCapacity']
        self.anActiveFrac = anParameters['anActiveFrac']
        self.anBinderFrac = anParameters['anBinderFrac']
        self.anConductorFrac = anParameters['anConductorFrac']

    def get_elyteParameters(self, elyteParameters):
        self.elyte_costPerCell = elyteParameters['elyte_costPerCell']

    def get_canParameters(self, canParameters):
        self.can_costPerCell = canParameters['can_costPerCell']

    def get_separatorParameters(self, separatorParameters):
        self.separator_costPerCell = separatorParameters['separater_costPerCell']

    #Now that we have all the inputs, we can start calculating total amounts:
    def calc_activeMasses(self):
        self.cat_activeMass = (self.catLoading*.001) * (2*self.electrodeOneSidedArea) #g
        anCapacity = 0 #need to figure out formula for this


