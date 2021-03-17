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

import qgrid


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


class MapDisplay:

    imagery = basemap_to_tiles(basemaps.Esri.WorldImagery)
    imagery.base = True
    osm = basemap_to_tiles(basemaps.OpenStreetMap.Mapnik)
    osm.base = True

    def __init__(self):
        self.map_display = Map(center=(32.715, -117.1625), zoom=12,
                               layers=[MapDisplay.imagery, MapDisplay.osm],
                               layout=Layout(height="700px"),
                               scroll_wheel_zoom=True)

        self.map_display.add_control(LayersControl())

    def add_layer(self, gdf, name, key):

        business = list()
        for i, r in tqdm(gdf.iterrows()):
            marker = CircleMarker(location=(r.geometry.y, r.geometry.x), radius=5, stroke=False, fill_color="blue", fill_opacity=1.0)
            msg = HTML()
            msg.value = f"{r[key]}"
            marker.popup = msg
            business.append(marker)
            gdf['marker'] = marker
        gdf['marker'] = business

        business_cluster = MarkerCluster(markers=business, name='Businesses')
        self.map_display.add_layer(business_cluster)


    def add_bids(self, gdf):

        bids = GeoData(geo_dataframe = gdf,
                   style={'color': 'black', 'fillColor': '#3366cc', 'opacity':0.05, 'weight':1.9, 'dashArray':'2', 'fillOpacity':0.6},
                   hover_style={'fillColor': 'red' , 'fillOpacity': 0.2},
                   name = 'BIDs')

        self.map_display += bids

        bid_html = HTML('''Hover over a district''')
        bid_html.layout.margin = '0px 20px 20px 20 px'
        bid_control = WidgetControl(widget=bid_html, position='topright')

        def update_bid_html(feature, **kwargs):
            bid_html.value = f"<b>{feature['properties']['name']}"
    
        self.map_display.add_control(bid_control)  # does += work for this?

        bids.on_hover(update_bid_html)


# This one seems quite redundant, but maybe it is just this simple?
class GridDisplay:

    def __init__(self, gdf):

        self.qgrid = qgrid.show_grid(gdf, show_toolbar=True)

