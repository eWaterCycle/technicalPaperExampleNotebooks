from esmvalcore.experimental import get_recipe
import deepdiff
import copy
import pytest
from forcing import update_marrmot

TEST_CASES = [(case['params'], case['expected_diff']) for case in (
    {
        'params': {},
        'expected_diff': {},
    },
    {
        'params': {
            'startyear': 1234
        },
        'expected_diff': {
            'values_changed': {
                "root['diagnostics']['diagnostic_daily']['variables']['tas']['start_year']":
                {
                    'new_value': 1234,
                    'old_value': 1990
                },
                "root['diagnostics']['diagnostic_daily']['variables']['pr']['start_year']":
                {
                    'new_value': 1234,
                    'old_value': 1990
                },
                "root['diagnostics']['diagnostic_daily']['variables']['psl']['start_year']":
                {
                    'new_value': 1234,
                    'old_value': 1990
                },
                "root['diagnostics']['diagnostic_daily']['variables']['rsds']['start_year']":
                {
                    'new_value': 1234,
                    'old_value': 1990
                },
                "root['diagnostics']['diagnostic_daily']['variables']['rsdt']['start_year']":
                {
                    'new_value': 1234,
                    'old_value': 1990
                }
            }
        }
    },
    {
        'params': {
            'endyear': 4321
        },
        'expected_diff': {
            'values_changed': {
                "root['diagnostics']['diagnostic_daily']['variables']['tas']['end_year']":
                {
                    'new_value': 4321,
                    'old_value': 2018
                },
                "root['diagnostics']['diagnostic_daily']['variables']['pr']['end_year']":
                {
                    'new_value': 4321,
                    'old_value': 2018
                },
                "root['diagnostics']['diagnostic_daily']['variables']['psl']['end_year']":
                {
                    'new_value': 4321,
                    'old_value': 2018
                },
                "root['diagnostics']['diagnostic_daily']['variables']['rsds']['end_year']":
                {
                    'new_value': 4321,
                    'old_value': 2018
                },
                "root['diagnostics']['diagnostic_daily']['variables']['rsdt']['end_year']":
                {
                    'new_value': 4321,
                    'old_value': 2018
                }
            }
        }
    },
    {
        'params': {
            'forcings': ['ERA5']
        },
        'expected_diff': {
            'values_changed': {
                "root['diagnostics']['diagnostic_daily']['additional_datasets'][0]['dataset']":
                {
                    'new_value': 'ERA5',
                    'old_value': 'ERA-Interim'
                }
            },
            'iterable_item_removed': {
                "root['diagnostics']['diagnostic_daily']['additional_datasets'][1]":
                {
                    'dataset': 'ERA5',
                    'project': 'OBS6',
                    'tier': 3,
                    'type': 'reanaly',
                    'version': 1
                }
            }
        }
    },
    {
        'params': {
            'shapefile': 'Rhine/Rhine.shp'
        },
        'expected_diff': {
            'values_changed': {
                "root['preprocessors']['daily']['extract_shape']['shapefile']":
                {
                    'new_value': 'Rhine/Rhine.shp',
                    'old_value': 'Meuse/Meuse.shp'
                },
                "root['diagnostics']['diagnostic_daily']['scripts']['script']['basin']":
                {
                    'new_value': 'Rhine',
                    'old_value': 'Meuse'
                }
            }
        }
    },
)]


@pytest.mark.parametrize('params, expected_diff', TEST_CASES)
def test_forcing_marrmot(params, expected_diff):
    recipe = get_recipe('hydrology/recipe_marrmot.yml')
    expected_data = recipe.data

    data = copy.deepcopy(expected_data)

    update_marrmot(data, **params)

    diff = deepdiff.DeepDiff(recipe.data, data)

    if not diff == expected_diff:
        raise AssertionError('\n' + diff.pretty())


if __name__ == '__main__':
    # generate differences
    params = {'startyear': 1234}
    recipe = get_recipe('hydrology/recipe_marrmot.yml')
    expected_data = recipe.data
    data = copy.deepcopy(expected_data)
    update_marmott(data, **params)
    diff = deepdiff.DeepDiff(recipe.data, data)
    print(diff)
