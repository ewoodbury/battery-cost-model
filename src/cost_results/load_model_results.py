from .models import CostResultsCell, CostResultsInfo,CostResultsKwh
from .cost_model_class import CostModel
from datetime import datetime
from django.utils.timezone import make_aware



def load_model_results(cell_instance, price_instance):
    '''Takes the selected cell and price inputs from the run_model page,
    runs the cost calculations with the CostModel class, and 
    uploads the cost results to the database using django interface.

    Inputs: 
    cell_instance is an instance of the costs.models.CellInput class.
    price_instance is an instance of the prices.models.PriceInput class.
    '''
    cost_model_instance = CostModel(cell_instance, price_instance)
    cost_model_instance.run_full_model()

    #CostResultsInfo Class:
    info_instance = CostResultsInfo()
    info_instance.model_version = cost_model_instance.MODEL_VERSION
    info_instance.date_created = make_aware(datetime.now())
    info_instance.cell_id = cost_model_instance.cellId
    info_instance.price_id = cost_model_instance.priceId
    #Saving to database:
    info_instance.save()

    #CostResultsCell Class:
    cell_instance = CostResultsCell()
    cell_instance.cat_active_material = cost_model_instance.cost_catActiveMaterial
    cell_instance.cat_binder = cost_model_instance.cost_catBinder
    cell_instance.cat_conductor = cost_model_instance.cost_catConductor
    cell_instance.an_active_material = cost_model_instance.cost_anActiveMaterial
    cell_instance.an_binder = cost_model_instance.cost_anBinder
    cell_instance.an_conductor = cost_model_instance.cost_anConductor
    cell_instance.al_foil = cost_model_instance.cost_alFoil
    cell_instance.cu_foil = cost_model_instance.cost_cuFoil
    cell_instance.can = cost_model_instance.cost_can
    cell_instance.sep = cost_model_instance.cost_separator
    cell_instance.elyte = cost_model_instance.cost_elyte
    cell_instance.manufacturing = cost_model_instance.cost_cellManufacturing
    cell_instance.pack_integration = cost_model_instance.cost_packIntegration
    #Saving to db:
    cell_instance.save()

    #CostResultsKwh Class:
    #First, define expression to multiply by number of cells per kwh:
    mult_by_cells = lambda a: a * cost_model_instance.cellsPerKwh
    kwh_instance = CostResultsKwh()
    kwh_instance.cat_active_material = mult_by_cells(cost_model_instance.cost_catActiveMaterial)
    kwh_instance.cat_binder = mult_by_cells(cost_model_instance.cost_catBinder)
    kwh_instance.cat_conductor = mult_by_cells(cost_model_instance.cost_catConductor)
    kwh_instance.an_active_material = mult_by_cells(cost_model_instance.cost_anActiveMaterial)
    kwh_instance.an_binder = mult_by_cells(cost_model_instance.cost_anBinder)
    kwh_instance.an_conductor = mult_by_cells(cost_model_instance.cost_anConductor)
    kwh_instance.al_foil = mult_by_cells(cost_model_instance.cost_alFoil)
    kwh_instance.cu_foil = mult_by_cells(cost_model_instance.cost_cuFoil)
    kwh_instance.can = mult_by_cells(cost_model_instance.cost_can)
    kwh_instance.sep = mult_by_cells(cost_model_instance.cost_separator)
    kwh_instance.elyte = mult_by_cells(cost_model_instance.cost_elyte)
    kwh_instance.manufacturing = mult_by_cells(cost_model_instance.cost_cellManufacturing)
    kwh_instance.pack_integration = mult_by_cells(cost_model_instance.cost_packIntegration)
    #Saving to db:
    kwh_instance.save()
    return "Results loaded successfully!"