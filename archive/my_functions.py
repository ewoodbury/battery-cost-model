def get_molar_mass(formula):
    element_mw = {
        'li':6.94,
        'ni':58.69,
        'mn':54.94,
        'co':58.93,
        'al':26.98,
        'o':16.00}
        
    molar_mass = 0
    for i in formula:
        molar_mass += formula[i]*element_mw[i]
    return molar_mass