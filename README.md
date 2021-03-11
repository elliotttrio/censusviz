# **censusviz -- map Census data**

This package helps users more easily visualize maps using Census Population Estimate API and the Census Cartographic GeoJSON boundary files. It transforms GeoJSON files into easy to work with GeoPandas.GeoDataFrame and plot choropleth maps.

## **How To Install**

Please install and import the censusviz package using the following commands. 
```
pip install censusviz
```

After installing via pip, please import the package to use on your Python IDE.

```
from censusviz import censusviz
```

## **Usage**

### Find Available Geo Parameters
The ```list_geoparams``` function returns a table from the Census' Github telling users which GeoJSON files are available by Year and geography area type. 

Parameters (optional):
- year: A string value of the year you would like to recall. %Y. Optional and will return a subset of table if specified.


```
censusviz.list_geoparams()

censusviz.list_geoparams(year = "2010")
```
### Return a Geopandas dataframe
The ```get_geocen_df``` function returns a geopandas.GeoDataFrame of Census cartographic files. 

Parameters:
 - quality: a string value of the resolution of the GeoJSON file. The available resolutions are 20m, 5m, and 500k.
- year:  a string value of the year you would like to recall. %Y. Year availables: 1990, 2000, 2010, 2012-2019.
- area_type: a stringe value of the geography area value you would like to specify. 

```
censusviz.get_geocen_df(quality = "20m", year = "2010", area_type= "county")
```
### Return State Identifiers
The ```get_state_ids``` function returns a pandas.DataFrame of state-related federal codes such as FIPS and USPS codes.

Parameters:
- state_initials: a string value of the officially recognized state abbreviation.

```
censusviz.get_state_ids(state_initials = "OR")

censusviz.get_state_ids(state_initials = "NY")
```
### Plot Cartographic shapes

The ```get_geocen_plot``` function returns a matplotlib.pyplot.plot of a specified cartographic area by year, area type and resolution quality.

Parameters
- quality: a string value of the resolution of the GeoJSON file. The available resolutions are 20m, 5m, and 500k.
- year:  a string value of the year you would like to recall. %Y. Years available: 1990, 2000, 2010, 2012-2019.
- area_type: a string value of the geography area value you would like to specify. 
- boundaries: a boolean value that if True returns only the outline/boundaries of the area specified and if false returns the whole area filled in.

```
censusviz.get_geocen_plot(quality ="20m", year="2010", area_type="county", boundaries=False)
```

### Return Population Data with Map 
The ```get_pop``` function  returns a choropleth map in matplotlib.pyplot.plot format or a geopandas.GeoDataFrame of the U.S. population by year and geometric boundaries. It utilizes the U.S. Census Bureau Population Estimate API and the Census GeoJSON database on GitHub.

Parameters
- api_key: a private api key provided by the U.S. Census Bureau. https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html 
- year:  a string value of the year you would like to recall. %Y. Year availables: 2015-2019.
- map: a boolean value that if True returns matplotlib.pyplot.plot of the area specified and if false returns a geopandas.GeoDataFrame of the same values.

```
censusviz.get_pop(api_key = my_api_key, year="2018", map = False)

censusviz.get_pop(api_key = my_api_key, year="2019", map = True)
```

![](https://github.com/elliotttrio/censusviz/blob/bb9fd0b0ca36843a051d9da57e4c5032af1561cd/screenshots/get_pop.PNG?raw=true)

### Return Population Data with Map (By Region)
The ```get_region_pop``` function function returns a choropleth map in matplotlib.pyplot.plot format or a geopandas.GeoDataFrame of the U.S. population by year and region. It utilizes the U.S. Census Bureau Population Estimate API and the Census GeoJSON database on GitHub.

Parameters
- api_key: a private api key provided by the U.S. Census Bureau. https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html 
- year:  a string value of the year you would like to recall. %Y. Year availables: 2018-2019.
- map: a boolean value that if True returns matplotlib.pyplot.plot of the area specified and if false returns a geopandas.GeoDataFrame for the same values.

```
censusviz.get_region_pop(api_key = my_api_key, year="2016", map = False)

censusviz.get_region_pop(api_key = my_api_key, year="2019", map = True)
```

![](https://github.com/elliotttrio/censusviz/blob/bb9fd0b0ca36843a051d9da57e4c5032af1561cd/screenshots/get_region_pop.PNG?raw=true)


### Return Population Data with Map (By State)
The ```get_state_pop``` function returns a choropleth map in matplotlib.pyplot.plot format or a geopandas.GeoDataFrame of the U.S. population by year and state. It utlizes the U.S. Census Bureau Population Estimate API and the Census GeoJSON database on GitHub.

 Parameters
 - api_key: a private api key provided by the U.S. Census Bureau. https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html 
- year:  a string value of the year you would like to recall. %Y. Year availables: 2018-2019.
- state_fip: a string value of the state Federal Information Processing Standard state code.
- map: a boolean value that if True returns matplotlib.pyplot.plot of the area specified and if false returns a geopandas.GeoDataFrame for the same values.

```
censusviz.get_state_pop(api_key = my_api_key, year="2016", state_fip = "15", map = False)

censusviz.get_state_pop(api_key = my_api_key, year="2019", state_fip = "29", map = True)
```

![](https://github.com/elliotttrio/censusviz/blob/bb9fd0b0ca36843a051d9da57e4c5032af1561cd/screenshots/get_state_pop.PNG?raw=true)

### Return Housing Unit Estimation Data with Map

The ```get_house_est``` returns a choropleth map in matplotlib.pyplot.plot format or a geopandas.GeoDataFrame of the U.S. housing estimates by year. It utlizes the U.S. Census Bureau Housing Unit Estimate API and the Census GeoJSON database on GitHub.

Parameters
- api_key: a private api key provided by the U.S. Census Bureau. https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html 
- year:  a string value of the year you would like to recall. %Y. Year availables: 2018-2019.
- map: a boolean value that if True returns matplotlib.pyplot.plot of the area specified and if false returns a geopandas.GeoDataFrame for the same values.

```
censusviz.get_house_est(api_key = my_api_key, year="2018", map = False)

censusviz.get_house_est(api_key = my_api_key, year="2019", map = True)
```

![](https://github.com/elliotttrio/censusviz/blob/bb9fd0b0ca36843a051d9da57e4c5032af1561cd/screenshots/get_house_est.PNG?raw=true)

## **Dependencies**

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

## **Documentation**

The official documentation is hosted on Read the Docs: https://censusviz.readthedocs.io/en/latest/

## **Contributors**

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/elliotttrio/censusviz/graphs/contributors).

### **Credits**

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
