import urllib.request
import json
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import lxml
import requests
from requests.exceptions import HTTPError

def list_geoparams(**kwargs):
    """
    This function returns a table from the Census' Github telling users which GeoJSON files are available by Year and geography area type. 

    Parameters
    ---
    year: A string value of the year you would like to recall. %Y. Optional and will return a subset of table if specified.

    Returns
    ---
    Output pandas.DataFrame of the webscrapped table with stated parameters
        Index: 
            RangeIndex
        Columns:
            Geographic Area Type: object
            1990: object
            2000: object
            2010: object
            2012: object
            2013 - 2015: object
            2016 - 2019: object

    Example
    ---
    censusviz.list_geoparams().shape
    (25,7)
    """
    try:
        df_list = pd.read_html('https://github.com/uscensusbureau/citysdk/blob/master/README.md')
        df_params = pd.DataFrame(df_list[2])
        df_table = df_params.replace('✔', 'Yes')
        for k in kwargs:
            year =  kwargs['year']
            if year == '2013' or year == '2014' or year == '2015':
                year = '2013 - 2015'
            elif year == '2016' or year == '2017' or year == '2018' or 'year' == '2019':
                year = '2016 - 2019'
            df_table = df_table[['Geographic Area Type', year]]
        return df_table
    except Exception as err:
        print(f'An error occured. If you specified a year, please make sure it is between 1990 and 2019: {err}')

def get_geocen_df(quality = str(), year = str(), area_type = str()):
    """
    This function returns a geopandas.GeoDataFrame of Census cartographic files. 

    Parameters
    ---
    quality: a string value of the resolution of the GeoJSON file. The available resolutions are 20m, 5m, and 500k.
    year:  a string value of the year you would like to recall. %Y. Year availables: 1990, 2000, 2010, 2012-2019.
    area_type: a stringe value of the geography area value you would like to specify. 

    Returns
    ---
    Output geopandas.GeoDataFrame of the API with stated parameters
        Index: 
            RangeIndex
        Columns:
            GEO_ID: object
            STATE: object
            COUNTY: object
            NAME: object
            LSAD: object
            CENSUSAREA: float64
            geometry: geometry
    
    Example
    ---
    censusviz.get_geocen_df(quality = "20m", year = "2010", area_type= "county").shape
    (3221, 7)

    """
    try:
        url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/{quality}/{year}/{area_type}.json"
        df = gpd.read_file(url)
        return df
    except Exception as err:
        print(f'An error occured. All parameters must be in string format and must exist in the Census GeoJSON database.: {err}')

def get_state_ids(state_initials = str()):
    """
    This function returns a pandas.DataFrame of state-related federal codes. 

    Parameters
    ---
    state_initials: a string value of the officially recognized state abbreviation.

    Returns
    ---
    Output pandas.DataFrame of the API with stated parameters
        Index: 
            RangeIndex
        Columns:
            NAME: object
            STUSPS: object
            STATEFP: object
            STATENS: object
            AFFGEOID: object
            GEOID: object
    
    Example
    ---
    censusviz.get_state_ids("OR").shape
    (1, 6)

    """
    try:
        quality = "20m"
        year = "2019"
        area_type = "state"
        state_initials = state_initials.upper()
        url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/{quality}/{year}/{area_type}.json"
        df = gpd.read_file(url)
        df = df[['NAME', 'STUSPS', 'STATEFP', 'STATENS', 'AFFGEOID', 'GEOID']]
        df = df[df.STUSPS == state_initials]
        return df
    except Exception as err:
        print(f'An error occured. Parameter must be in string format.: {err}')

def get_geocen_plot(quality = str(), year = str(), area_type = str(), boundaries = bool()):
    """
    This function returns a matplotlib.pyplot.plot of a specified cartographic area by year, area type and resolution quality.

    Parameters
    ---
    quality: a string value of the resolution of the GeoJSON file. The available resolutions are 20m, 5m, and 500k.
    year:  a string value of the year you would like to recall. %Y. Year availables: 1990, 2000, 2010, 2012-2019.
    area_type: a stringe value of the geography area value you would like to specify. 
    boundaries = a boolean value that if True returns only the outline/boundaries of the area specified and if false returns the whole are filled in.

    Returns
    ---
    Output matplotlib.pyplot.plot of the geometric information with stated parameters.

    Example
    ---
    censusviz.get_geocen_plot(quality ="20m", year="2010", area_type="county", boundaries=False)

    """
    try:
        url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/{quality}/{year}/{area_type}.json"
        df = gpd.read_file(url)
        if boundaries == True:
            return df.boundary.plot()
        else:
            return df.plot()
    except Exception as err:
        print(f'An error occured. All parameters must exist in the Census GeoJSON database. Please check https://github.com/uscensusbureau/citysdk/tree/master/v2/GeoJSON: {err}')

def get_pop(api_key, year = str(), map = bool()):
    """
    This function returns a choropleth map in matplotlib.pyplot.plot format or a geopandas.GeoDataFrame of the U.S. population by year. It utlizes the U.S. Census Bureau Population Estimate API and the Census GeoJSON database on GitHub.

    Parameters
    ---
    api_key: a private api key provided by the U.S. Census Bureau. https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html 
    year:  a string value of the year you would like to recall. %Y. Year availables: 2015-2019.
    map = a boolean value that if True returns matplotlib.pyplot.plot of the area specified and if false returns a geopandas.GeoDataFrame for the same values.

    Returns
    ---
    Output geopandas.GeoDataFrame or a matplotlib.pyplot.plot object of the geometric information with stated parameters.

    STATEFP:object
    STATENS:object
    AFFGEOID:object
    GEOID:object
    STUSPS:object
    NAME:object
    LSAD:object
    ALAND:int64
    AWATER:int64
    geometry:geometry
    Pop_Count:int32

    Example
    ---
    censusviz.get_pop(api_key = my_api_key, year="2018", map = False)
    censusviz.get_pop(api_key = my_api_key, year="2019", map = True)

    """
    try:
        year = year
        pop_url = f'http://api.census.gov/data/{year}/pep/population?get=POP&for=state:*&key={api_key}'
        r = requests.get(pop_url)
        data = json.loads(r.content) 
        pop_df = pd.DataFrame(data[1:], columns=data[0]).\
            rename(columns={"POP": "Pop_Count", "state": "STATEFP"})
        pop_df['Pop_Count'] = pop_df['Pop_Count'].astype(str).astype(int)
        geodata_url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/20m/{year}/state.json"
        geo_df = gpd.read_file(geodata_url)
        geo_df = geo_df.merge(pop_df, on = 'STATEFP')
        if map == True:
            return geo_df.plot(column = 'Pop_Count')
        else:
            return geo_df
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occured. All parameters must exist in the Census GeoJSON database. Please check https://github.com/uscensusbureau/citysdk/tree/master/v2/GeoJSON: {err}')

def get_house_est(api_key, year = str(), map = bool()):
    """
    This function returns a choropleth map in matplotlib.pyplot.plot format or a geopandas.GeoDataFrame of the U.S. housing estimates by year. It utlizes the U.S. Census Bureau Housing Unit Estimate API and the Census GeoJSON database on GitHub.

    Parameters
    ---
    api_key: a private api key provided by the U.S. Census Bureau. https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html 
    year:  a string value of the year you would like to recall. %Y. Year availables: 2018-2019.
    map = a boolean value that if True returns matplotlib.pyplot.plot of the area specified and if false returns a geopandas.GeoDataFrame for the same values.

    Returns
    ---
    Output geopandas.GeoDataFrame or a matplotlib.pyplot.plot object of the geometric information with stated parameters.
    STATEFP:object
    STATENS:object
    AFFGEOID:object
    GEOID:object
    STUSPS:object
    NAME:object
    LSAD:object
    ALAND:int64
    AWATER:int64
    geometry:geometry
    Housing_Estimates:int32

    Example
    ---
    censusviz.get_house_est(api_key = my_api_key, year="2018", map = False)
    censusviz.get_house_est(api_key = my_api_key, year="2019", map = True)

    """
    try:
        house_url = f'http://api.census.gov/data/{year}/pep/housing?get=HUEST&for=state:*&key={api_key}'
        r = requests.get(house_url)
        data = json.loads(r.content) 
        house_df = pd.DataFrame(data[1:], columns=data[0]).\
            rename(columns={"HUEST": "Housing_Estimates", "state": "STATEFP"})
        house_df['Housing_Estimates'] = house_df['Housing_Estimates'].astype(str).astype(int)
        geodata_url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/20m/{year}/state.json"
        geo_df = gpd.read_file(geodata_url)
        geo_df = geo_df.merge(house_df, on = 'STATEFP')
        if map == True:
            return geo_df.plot(column = 'Housing_Estimates')
        else:
            return geo_df
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occured. All parameters must exist in the Census GeoJSON database and API. Please check https://github.com/uscensusbureau/citysdk/tree/master/v2/GeoJSON: {err}')

def get_region_pop(api_key, year = str(), map = bool()):
    """
    This function returns a choropleth map in matplotlib.pyplot.plot format or a geopandas.GeoDataFrame of the U.S. population by year and region. It utlizes the U.S. Census Bureau Population Estimate API and the Census GeoJSON database on GitHub.

    Parameters
    ---
    api_key: a private api key provided by the U.S. Census Bureau. https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html 
    year:  a string value of the year you would like to recall. %Y. Year availables: 2018-2019.
    map = a boolean value that if True returns matplotlib.pyplot.plot of the area specified and if false returns a geopandas.GeoDataFrame for the same values.

    Returns
    ---
    Output geopandas.GeoDataFrame or a matplotlib.pyplot.plot object of the geometric information with stated parameters.

    REGIONCE:object
    AFFGEOID:object
    GEOID:object
    NAME:object
    LSAD:object
    ALAND:int64
    AWATER:int64
    geometry:geometry

    Example
    ---
    censusviz.get_region_pop(api_key = my_api_key, year="2016", map = False)
    censusviz.get_region_pop(api_key = my_api_key, year="2019", map = True)

    """
    try:
        year = year
        pop_url = f'http://api.census.gov/data/{year}/pep/population?get=POP&for=REGION:*&key={api_key}'
        r = requests.get(pop_url)
        data = json.loads(r.content) 
        pop_df = pd.DataFrame(data[1:], columns=data[0]).\
            rename(columns={"POP": "Pop_Count", "region": "REGIONCE"})
        pop_df['Pop_Count'] = pop_df['Pop_Count'].astype(str).astype(int)
        geodata_url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/20m/{year}/region.json"
        geo_df = gpd.read_file(geodata_url)
        geo_df = geo_df.merge(pop_df, on = 'REGIONCE')
        if map == True:
            return geo_df.plot(column = 'Pop_Count')
        else:
            return geo_df
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occured. All parameters must exist in the Census GeoJSON database and API. Please check https://github.com/uscensusbureau/citysdk/tree/master/v2/GeoJSON: {err}')

def get_state_pop(api_key, year = str(), state_fip = str(), map = bool()):
    """
    This function returns a choropleth map in matplotlib.pyplot.plot format or a geopandas.GeoDataFrame of the U.S. population by year and state. It utlizes the U.S. Census Bureau Population Estimate API and the Census GeoJSON database on GitHub.

    Parameters
    ---
    api_key: a private api key provided by the U.S. Census Bureau. https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html 
    year:  a string value of the year you would like to recall. %Y. Year availables: 2018-2019.
    state_fip: a string value of the state Federal Information Processing Standard state code.
    map = a boolean value that if True returns matplotlib.pyplot.plot of the area specified and if false returns a geopandas.GeoDataFrame for the same values.

    Returns
    ---
    Output geopandas.GeoDataFrame or a matplotlib.pyplot.plot object of the geometric information with stated parameters.

    STATE_FIP:object
    COUNTYFP:object
    COUNTYNS:object
    AFFGEOID:object
    GEOID:object
    NAME:object
    LSAD:object
    ALAND:int64
    AWATER:int64
    geometry:geometry
    Pop_Count:int32

    Example
    ---
    censusviz.get_state_pop(api_key = my_api_key, year="2016", state_fip = "15", map = False)
    censusviz.get_state_pop(api_key = my_api_key, year="2019", state_fip = "29", map = True)

    """
    try:
        pop_url = f'http://api.census.gov/data/{year}/pep/population?get=POP&for=COUNTY&in=state:*&key={api_key}'
        r = requests.get(pop_url)
        data = json.loads(r.content) 
        pop_df = pd.DataFrame(data[1:], columns=data[0]).\
            rename(columns={"POP": "Pop_Count", "state": "STATEFP", "county": "COUNTYFP"})
        pop_df['Pop_Count'] = pop_df['Pop_Count'].astype(str).astype(int)
        pop_df = pop_df[pop_df.STATEFP == state_fip]
        geodata_url = f"https://raw.githubusercontent.com/uscensusbureau/citysdk/master/v2/GeoJSON/20m/{year}/county.json"
        geo_df = gpd.read_file(geodata_url)
        geo_df = geo_df[geo_df.STATEFP == state_fip]
        geo_df = geo_df.merge(pop_df, on = 'COUNTYFP')
        geo_df.drop(geo_df.filter(regex='_y$').columns.tolist(),axis=1, inplace=True)
        geo_df = geo_df.rename(columns = {'STATEFP_x':'STATE_FIP'})
        if map == True:
            return geo_df.plot(column = 'Pop_Count')
        else:
            return geo_df
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occured. All parameters must exist in the Census GeoJSON database and API. Please check https://github.com/uscensusbureau/citysdk/tree/master/v2/GeoJSON: {err}')
