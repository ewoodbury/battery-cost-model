from my_functions import get_molar_mass

class Model:

    # Initializer:
    def __init__(self, model_id):
        self.model_id = model_id

    ## Section 1: Importing Cell Parameters
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

    def get_currentcollectorParameters(self,currentcollectorParameters):
        self.alFoilThickness = currentcollectorParameters['alFoilThickness'] #um
        self.cuFoilThickness = currentcollectorParameters['cuFoilThickness'] #um

    def get_elyteParameters(self, elyteParameters):
        self.elyteCostPerCell = elyteParameters['elyteCostPerCell']

    def get_canParameters(self, canParameters):
        self.canCostPerCell = canParameters['canCostPerCell']

    def get_separatorParameters(self, separatorParameters):
        self.separatorCostPerCell = separatorParameters['separatorCostPerCell']

    def get_echemParameters(self,echemParameters):
        self.avgDischargeVoltage = echemParameters['avgDischargeVoltage']

    # Get all input parameters:
    def get_allParameters(self, allParameters):
        '''Retrieves all input parameters by calling the retreival function for each 
        individual cell component'''
        self.get_genParameters(allParameters['genParameters'])
        self.get_catParameters(allParameters['catParameters'])
        self.get_anParameters(allParameters['anParameters'])
        self.get_currentcollectorParameters(allParameters['currentcollectorParameters'])
        self.get_elyteParameters(allParameters['elyteParameters'])
        self.get_canParameters(allParameters['canParameters'])
        self.get_separatorParameters(allParameters['separatorParameters'])
        self.get_echemParameters(allParameters['echemParameters'])

    ##################################################################################
    ## Section 2: Importing Price Data
    def get_materialPrices(self, price_materials):
        self.price_catActiveMaterial = price_materials['price_catActiveMaterial']
        self.price_catBinder = price_materials['price_catBinder']
        self.price_catConductor = price_materials['price_catConductor']
        self.price_anActiveMaterial = price_materials['price_anActiveMaterial']
        self.price_anBinder = price_materials['price_anBinder']
        self.price_anConductor = price_materials['price_anConductor']
        self.price_alFoil = price_materials['price_alFoil']
        self.price_cuFoil = price_materials['price_cuFoil']
        self.price_can = price_materials['price_can']
        self.price_separator = price_materials['price_separator']
        self.price_elyte = price_materials['price_elyte']

    def get_manufacturingPrices(self, price_manufacturing):
        self.price_cellManufacturing = price_manufacturing['price_cellManufacturing']
        self.price_packIntegration = price_manufacturing['price_packIntegration']

    # Get all prices
    def get_allPrices(self,allPrices):
        self.get_materialPrices(allPrices['price_materials'])
        self.get_manufacturingPrices(allPrices['price_manufacturing'])

    ##################################################################################
    ## Section 3: Preliminary Calculations
    # Calculating total electrode material masses:
    def calc_electrodeMasses(self):
        '''Calculates total cathode and anode mass, as well as active mass, 
        binder mass, and conductor mass for each electrode
        '''
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

    def calc_currentCollectorMasses(self):
        al_density = 2.70 #g/cm^3
        cu_density = 8.96 #g/cm^3
        self.mass_alFoil = self.electrodeOneSidedArea * (self.alFoilThickness/1e4) * al_density #g
        self.mass_cuFoil = self.electrodeOneSidedArea * (self.cuFoilThickness/1e4) * cu_density #g

    def calc_separatorLength(self):
        self.separatorLength = self.electrodeLength #cm

    # Aggregating data to calculate cell energy and cells per kWh
    def calc_cellEnergy(self):
        '''Calculates the energy per cell (in Wh) given the cell capacity (in mAh)
        and average discharge voltage (in V). 
        Note that this uses cathode capacity for the calculation, given that the 
        cathode has a lower capacity than the anode (because the N-P ratio should 
        always be greater than 1).
        '''
        self.cellEnergy = (self.catCellCapacity/1000) * self.avgDischargeVoltage

    def calc_cellsPerKwh(self):
        '''Calculates number of cells per 1 kWh of energy.
        
        Input: self.cellEnergy (cell energy in Wh)
        Output: Number of cells requred to have 1kWh of energy.
        This metric is very useful when caculating costs on a per kWh basis.
        '''
        self.cellsPerKwh = 1000/self.cellEnergy

    #Calculate all preliminary values:
    def calc_allPreliminary(self):
        self.calc_electrodeMasses()
        self.calc_currentCollectorMasses()
        self.calc_separatorLength()
        self.calc_cellEnergy()
        self.calc_cellsPerKwh()

    ##################################################################################
    ## Section 4: Cost Calculations
    # All cost calculations here are on a cost per cell basis.
    def calc_cost_cat(self):
        self.cost_catActiveMaterial = (self.catActiveMass/1000) * self.price_catActiveMaterial
        self.cost_catBinder = (self.catBinderMass/1000) * self.price_catBinder
        self.cost_catConductor = (self.catConductorMass/1000) * self.price_catConductor
        self.cost_catTotal = self.cost_catActiveMaterial + self.cost_catBinder + self.cost_catConductor

    def calc_cost_an(self):
        self.cost_anActiveMaterial = (self.anActiveMass/1000) * self.price_anActiveMaterial
        self.cost_anBinder = (self.anBinderMass/1000) * self.price_anBinder
        self.cost_anConductor = (self.anConductorMass/1000) * self.price_anConductor
        self.cost_canTotal = self.cost_anActiveMaterial + self.cost_anBinder + self.cost_anConductor

    def calc_cost_currentCollectors(self):
        self.cost_alFoil = (self.mass_alFoil/1000) * self.price_alFoil
        self.cost_cuFoil = (self.mass_cuFoil/1000) * self.price_cuFoil

    def calc_cost_can(self):
        self.cost_can = self.canCostPerCell

    def calc_cost_separator(self):
        # First: calculate price per cm of length
        # Divide by 500 for 500m per separtor roll, then by 100 for 100cm per m
        pricePerCm_separator = self.price_separator / (500 * 100)
        self.cost_separator = pricePerCm_separator * self.electrodeLength

    def calc_cost_elyte(self):
        self.cost_elyte = self.price_elyte

    def calc_cost_manufacturing(self):
        self.cost_cellManufacturing = self.price_cellManufacturing
        self.cost_packIntegration = self.price_packIntegration

    # Calculate all cost values:
    def calc_allCosts(self):
        self.calc_cost_cat()
        self.calc_cost_an()
        self.calc_cost_currentCollectors()
        self.calc_cost_can()
        self.calc_cost_separator()
        self.calc_cost_elyte()
        self.calc_cost_manufacturing()

    



    


    




