from esmvalcore.experimental import get_recipe

BASINS = {
    'Doring': 'Doring/Doring.shp',
    'Great_Kei': 'Great_Kei/Great_Kei.shp',
    'Merrimack': 'Merrimack/Merrimack.shp',
    'Meuse': 'Meuse/Meuse.shp',
    'Rhine': 'Rhine/Rhine.shp',
    'Savannah': 'Savannah/Savannah.shp',
}

FORCINGS = {
    'ERA5': {
        'dataset': 'ERA5',
        'project': 'OBS6',
        'tier': 3,
        'type': 'reanaly',
        'version': 1
    },
    'ERA-Interim': {
        'dataset': 'ERA-Interim',
        'project': 'OBS6',
        'tier': 3,
        'type': 'reanaly',
        'version': 1
    },
}


def update_hype(data: dict, **kwargs):
    """
    Update marmott recipe data in-place.
    """
    raise NotImplementedError


def update_lisflood(data: dict, **kwargs):
    """
    Update marmott recipe data in-place.
    """
    raise NotImplementedError


def update_marrmot(
    data: dict,
    *,
    forcings: list = None,
    startyear: int = None,
    endyear: int = None,
    basin: str = None,
):
    """
    Update marmott recipe data in-place.

    Parameters
    ----------
    forcings : list
        List of forcings to use
    startyear : int
        Start year for the observation data
    endyear : int
        End year for the observation data
    basin : str
        Name of the basin to use. Defines the shapefile.
    """
    if basin is not None:
        shapefile = BASINS[basin]
        data['preprocessors']['daily']['extract_shape'][
            'shapefile'] = shapefile
        data['diagnostics']['diagnostic_daily']['scripts']['script'][
            'basin'] = basin

    if forcings is not None:
        datasets = [FORCINGS[forcing] for forcing in forcings]
        data['diagnostics']['diagnostic_daily'][
            'additional_datasets'] = datasets

    if startyear is not None:
        data['diagnostics']['diagnostic_daily']['variables']['tas'][
            'start_year'] = startyear
        data['diagnostics']['diagnostic_daily']['variables']['pr'][
            'start_year'] = startyear
        data['diagnostics']['diagnostic_daily']['variables']['psl'][
            'start_year'] = startyear
        data['diagnostics']['diagnostic_daily']['variables']['rsds'][
            'start_year'] = startyear
        data['diagnostics']['diagnostic_daily']['variables']['rsdt'][
            'start_year'] = startyear

    if endyear is not None:
        data['diagnostics']['diagnostic_daily']['variables']['tas'][
            'end_year'] = endyear
        data['diagnostics']['diagnostic_daily']['variables']['pr'][
            'end_year'] = endyear
        data['diagnostics']['diagnostic_daily']['variables']['psl'][
            'end_year'] = endyear
        data['diagnostics']['diagnostic_daily']['variables']['rsds'][
            'end_year'] = endyear
        data['diagnostics']['diagnostic_daily']['variables']['rsdt'][
            'end_year'] = endyear

    return data


def update_pcrglobwb(data: dict, **kwargs):
    """
    Update marmott recipe data in-place.
    """
    raise NotImplementedError


def update_wflow(data: dict, **kwargs):
    """
    Update marmott recipe data in-place.
    """
    raise NotImplementedError


MODEL_DATA = {
    'hype': {
        'recipe_name': 'hydrology/recipe_hype.yml',
        'update_func': update_hype,
    },
    'lisflood': {
        'recipe_name': 'hydrology/recipe_lisflood.yml',
        'update_func': update_lisflood,
    },
    'marrmot': {
        'recipe_name': 'hydrology/recipe_marrmot.yml',
        'update_func': update_marrmot,
    },
    'pcrglobwb': {
        'recipe_name': 'hydrology/recipe_pcrglobwb.yml',
        'update_func': update_pcrglobwb,
    },
    'wflow': {
        'recipe_name': 'hydrology/recipe_wflowyml',
        'update_func': update_wflow,
    },
}


def generate(model: str, **kwargs):
    """
    Parameters
    ----------
    model : str
        Name of the model
    **kwargs :
        Model specific parameters
    """
    model_data = MODEL_DATA[model]
    recipe_name = model_data['recipe_name']
    recipe = get_recipe(recipe_name)

    update_func = model_data['update_func']
    update_func(recipe.data, **kwargs)
    recipe.run()
