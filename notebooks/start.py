#%matplotlib inline
#%matplotlib widget
import warnings
#warnings.filterwarnings('ignore')

import base64
import datetime
import json
import sys

import requests
from tqdm import tqdm

import pandas as pd
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
from shapely.geometry import Point, MultiPolygon, Polygon, LineString

import networkx as nx
import osmnx as ox
ox.config(use_cache=True, log_console=True)

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
plt.style.use('bmh')


from IPython.display import IFrame, Markdown

from ipywidgets import Layout, HTML, Text, interact

from ipyleaflet import (Map, Rectangle, GeoJSON,
                        MarkerCluster, GeoData, LayersControl,
                        LayerGroup, Marker, WidgetControl,
                        CircleMarker,
                       basemaps, basemap_to_tiles)

from bqplot import pyplot as plt
from bqplot import (LinearScale, LogScale, OrdinalScale, ColorScale,
                    Scatter,
                    Figure,
                    ColorScale,
                    Bars,
                    )

#sys.path.append('/home/mcmorgan/projects/projects.geo/opensd/src')
#sys.path.append('/home/mcmorgan/projects/projects.geo/cityiqaccess')

sys.path.append('../src')
