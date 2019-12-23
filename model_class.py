from my_functions import get_molar_mass

class Model:

    # Initializer:
    def __init__(self, model_id):
        self.model_id = model_id

    # Now: define method to extract input parameters from input dictionaries
    def get_genParameters(self, genParameters):
        self.cellType = genParameters['cellType']
        self.npRatio = genParameters['npRatio']
        self.electrodeLength = genParameters['electrodeLength'] #cm
        self.electrodeWidth = genParameters['electrodeWidth'] #cm
        self.electrodeOneSidedArea = self.electrodeLength*self.electrodeWidth #cm
        
    def get_catParameters(self, catParameters):
        self.catFormula = catParameters['catFormula'] #Chemical formula as dictionary
        self.catGravCapacity = catParameters['catGravCapacity'] #mAh/g
        self.catTotalLoading = catParameters['catTotalLoading'] #mg/cm^2
        self.catActiveFrac = catParameters['catActiveFrac']
        self.catBinderFrac = catParameters['catBinderFrac']
        self.catConductorFrac = catParameters['catConductorFrac']
    
    def get_anParameters(self, anParameters):
        self.anGravCapacity = anParameters['anGravCapacity'] #mAh/g
        self.anActiveFrac = anParameters['anActiveFrac']
        self.anBinderFrac = anParameters['anBinderFrac']
        self.anConductorFrac = anParameters['anConductorFrac']

    def get_elyteParameters(self, elyteParameters):
        self.elyteCostPerCell = elyteParameters['elyteCostPerCell']

    def get_canParameters(self, canParameters):
        self.canCostPerCell = canParameters['canCostPerCell']

    def get_separatorParameters(self, separatorParameters):
        self.separatorCostPerCell = separatorParameters['separatorCostPerCell']

    def get_currentcollectorParameters(self,currentcollectorParameters):
        self.alThickness = currentcollectorParameters['alThickness'] #um
        self.cuThickness = currentcollectorParameters['cuThickness'] #um

    def get_echemParameters(self,echemParameters):
        self.avgDischargeVoltage = echemParameters['avgDischargeVoltage']

    # Defining a method to extract all input parameters:
    def get_allParameters(self, allParameters):
        '''Retrieves all input parameters by calling the retreival function for each 
        individual cell component'''
        self.get_genParameters(allParameters['genParameters'])
        self.get_catParameters(allParameters['catParameters'])
        self.get_anParameters(allParameters['anParameters'])
        self.get_elyteParameters(allParameters['elyteParameters'])
        self.get_canParameters(allParameters['canParameters'])
        self.get_separatorParameters(allParameters['separatorParameters'])
        self.get_echemParameters(allParameters['echemParameters'])


    # Now that we have all the inputs, we can start calculating total amounts:
    def calc_electrodeMasses(self):
        '''Calculates total cathode and anode mass, as well as active mass, 
        binder mass, and conductor mass for each electrode'''
        self.catTotalMass = (self.catTotalLoading*.001) * (2*self.electrodeOneSidedArea) #g
        self.catActiveMass = self.catTotalMass * self.catActiveFrac #g
        self.catCellCapacity = self.catActiveMass * self.catGravCapacity #mAh per cell
        self.anCellCapacity = self.npRatio * self.catCellCapacity #mah per cell
        self.anActiveMass = self.anCellCapacity / self.anGravCapacity #g
        self.anTotalMass = self.anActiveMass / self.anActiveFrac #g

        self.catBinderMass = self.catTotalMass * self.catBinderFrac
        self.catConductorMass = self.catTotalMass * self.catConductorFrac
        self.anBinderMass = self.anTotalMass * self.anBinderFrac
        self.anConductorMass = self.anTotalMass * self.anConductorFrac

    def calc_cellEnergy(self):
        '''Calculates the energy per cell (in Wh) given the cell capacity (in mAh)
        and average discharge voltage (in V). 
        Note that this uses cathode capacity for the calculation, given that the 
        cathode has a lower capacity than the anode (because the N-P ratio should 
        always be greater than 1).'''
        self.cellEnergy = (self.catCellCapacity/1000) * self.avgDischargeVoltage

    def calc_cellsPerKwh(self):
        '''Calculates number of cells needed to have 1 kWh of energy, given the 
        cell energy (in Wh) as an input. This metric is very useful when caculating
        costs on a per kWh basis.'''
        self.cellsPerKwh = 1000/self.cellEnergy

    # Next up: Importing price data
    def get_catPrice(self, catPrice):
        



