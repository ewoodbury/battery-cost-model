genParameters = {
    'cellType':'18650',
    'npRatio':1.02,
    'electrodeLength':110, #cm
    'electrodeWidth':5.5 #cm
    } 

catFormula = {'li':1,'ni':.333,'mn':.333,'co':.333,'al':0,'o':2}
catParameters = {
    'catFormula':catFormula,
    'catGravCapacity': 160, #mAh/g
    'catTotalLoading': 25, #mg/cm2
    'catActiveFrac': .98,
    'catBinderFrac': .01,
    'catConductorFrac': .01
    }

anParameters = {
    'anGravCapacity': 360, #mAh/g
    'anActiveFrac': .98,
    'anBinderFrac': .02,
    'anConductorFrac': 0
    }

elyteParameters = {'elyteCostPerCell':0.2}
separatorParameters = {'separatorCostPerCell':.05}
canParameters = {'canCostPerCell':.25}
currentcollectorParameters = {
    'alFoilThickness':20, #um
    'cuFoilThickness':10 #um
    }
echemParameters = {'avgDischargeVoltage':3.6}

allParameters = {
    'genParameters':genParameters,
    'catParameters':catParameters,
    'anParameters':anParameters,
    'elyteParameters':elyteParameters,
    'canParameters':canParameters,
    'separatorParameters':separatorParameters,
    'echemParameters':echemParameters
    }