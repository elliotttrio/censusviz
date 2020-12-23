from censusviz import __version__
from censusviz import censusviz

def test_version():
    assert __version__ == '0.1.0'

import geopandas as gpd
import urllib.request
import json
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import lxml
import requests
from requests.exceptions import HTTPError

def test_version():
    assert __version__ == '0.1.0'

def test_list_geoparams():
    geoparams_df = censusviz.list_geoparams()
    assert type(geoparams_df) == pd.core.frame.DataFrame

def test_get_geocen_df():
    df = censusviz.get_geocen_df(quality = "20m", year = "2010", area_type= "county")
    assert df.shape == (3221, 7)

def test_get_state_ids():
    geoID = censusviz.get_state_ids(state_initials = "OR")
    assert type(geoID) == pd.core.frame.DataFrame