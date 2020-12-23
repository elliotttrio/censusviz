# censusviz 

![](https://github.com/elliotttrio/censusviz/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/elliotttrio/censusviz/branch/main/graph/badge.svg)](https://codecov.io/gh/elliotttrio/censusviz) ![Release](https://github.com/elliotttrio/censusviz/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/censusviz/badge/?version=latest)](https://censusviz.readthedocs.io/en/latest/?badge=latest)

This package helps users more easily visualize maps using Census Population Estimate API and the Census Cartographic GeoJSON boundary files. It transforms GeoJSON files into easy to work with GeoPandas.GeoDataFrame and plot choropleth maps.

## Installation

```bash
pip install censusviz
```
## Dependencies

- python = "^3.6"
- pandas 
- pyproj 
- requests 
- numpy 
- shapely 
- gdal = [Wheels for Windows User](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal)
- fiona = [Wheels for Windows User](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona)
- geopandas 
- matplotlib 
- descartes 
- lxml

## Usage

```jupyter
from censusviz import censusviz

# example functions

geocenpy.list_geoparams()

geocenpy.get_geocen_df(quality = "20m", year = "2010", area_type= "county")

geocenpy.get_geocen_plot(quality ="20m", year="2010", area_type="county", boundaries=False)

geocenpy.get_pop(api_key = my_api_key, year="2019", map = True)

geocenpy.get_house_est(api_key = my_api_key, year="2019", map = True)

geocenpy.get_region_pop(api_key = my_api_key, year="2019", map = True)

geocenpy.get_state_pop(api_key = my_api_key, year="2019", state_fip = "29", map = True)

```

## Documentation

The official documentation is hosted on Read the Docs: https://censusviz.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/elliotttrio/censusviz/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
