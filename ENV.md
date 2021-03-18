# Notes on the env

I use jupyter lab with ipywidgets, ipyleaflet, bqplot, and qgrid. Here's a simple recipe to set it up from scratch.  

  1. Make sure Anaconda is installed and clone the repository from github.  cd into the workshop folder.  
  
  2. In the workshop folder you should see the environment.yml file.  Use this to build the env using conda:  `conda env create -f environment.yml`
  
  3. Once the create env is completed, activate the new env: `conda activate workshop`
  
  4. Now that you're in the workshop env,  set up the js packages with: `jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet bqplot qgrid2`
  
  5. At this point you will have a working jupyter lab with the necessary widgets.  Launch the lab with `juptyer lab`.
  
  6. You're ready to explore, understand, develop, ...
  
