price_materials = {
    'price_catActiveMaterial':60, # USD/kg, https://www.alibaba.com/product-detail/Lithium-Nickel-Manganese-Cobalt-Oxide-LiNiMnCoO2_62095939891.html
    'price_catBinder':0, #USD/kg
    'price_catConductor':0, #USD/kg
    'price_anActiveMaterial':20, #USD/kg, https://www.alibaba.com/product-detail/216-A-99-95-CAS-7782_62183988180.html
    'price_anBinder':0, #USD/kg
    'price_anConductor':0, #USD/kg
    'price_alFoil':5, #USD/kg for 20um thickness roll, https://www.alibaba.com/product-detail/Li-ion-battery-basic-materials-current_1581959679.html
    'price_cuFoil':10, #USD/kg for 10um thickness roll, https://www.alibaba.com/product-detail/High-purity-copper-foil-supplier-for_785875718.html
    'price_can':0.20, # USD/can (1 can = 1 cell)
    'price_separator':60, #USD/roll; One roll is 500m long, https://www.alibaba.com/product-detail/Fiberglass-Polypropylene-Material-Li-ion-Battery_60565640459.html
    'price_elyte':0.20 # USD/18650 cell; will add volume cost later
}

price_manufacturing = {
    'price_cellManufacturing':0, # USD/cell
    'price_packIntegration':0 # USD/cell
}

allPrices = {
    'price_materials':price_materials,
    'price_manufacturing':price_manufacturing
}