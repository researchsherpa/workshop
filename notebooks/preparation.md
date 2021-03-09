# Preparation

This repository is a  collection of notebooks providing a quick look at this data.  They demonstrate an approach to combine different open source information to analyze, filter, query, and visualize the data.

## Initial use cases
Initial **questions** focus on entities: **business type and location**,  localities: **neighorhoods, and Business Improvement Districts** and national/regional areas: **Census, BLS, council districts, and [employment centers](https://www.sandag.org/index.asp?classid=16&subclassid=127&projectid=581&fuseaction=projects.detail)** of San Diego.<br/>

Specific cases to start with:

  1. Clean and analyze the **[scalesd business csv](https://onedrive.live.com/edit.aspx?resid=1E5F39F3051216FA!217&cid=af24648a-ad9d-4a64-91f2-1c89990698c1&ithint=file%2cxlsx&wdOrigin=OFFICECOM-WEB.START.MRU)**.
  2. Geocode business data with **[OSM Nominatim](https://nominatim.openstreetmap.org/ui/search.html)**.
  3. Use shape files from City of SD to filter for different [BID](https://www.sandiego.gov/economic-development/about/bids)s.
  2. [jupyterlab](https://jupyter.org/) and multiple py packages for analysis and visualization.

## Data
The analysis combines multiple sources for **context**.  Specifically:<br/>

  1. Open government polygon data as a foundation.
  2. Business data from `scalesd`.
  3. [osm for geocoding and street networks](https://geoffboeing.com/2016/11/osmnx-python-street-networks/).
  4. [City of SD](https://data.sandiego.gov/) and [sangis](https://sangis.org/download/index.html) for various shape files, specifically the [BID](https://data.sandiego.gov/datasets/business-improvement-districts/) data.

## Tools and Techniques
Tools, techniques, and use cases to discuss at this time:

  1. `jupyterlab` (with a bit of emacs) is my development environment.
  2. `pandas, geopandas, and shapely` for spatial analysis.
  3. `ipyleaflet`, bqplot, and `ipywidgets` for mapping and dashboard development.
  4. `osmnx` for geocoding (via **OSM**).
  
## Issues

  1. The workflow has become a bit fractured with this tool based thinking!
  2. I think a good mechanism to validate NAICS would be cool.
  3. I am going to start working a `story`.

