#!/bin/bash

~/conda/bin/conda install -y \
      jupyter \
      seaborn plotly \
      scikit-learn scikit-image \
      dask dask-image \
      beautifulsoup4

~/conda/bin/conda install -yc conda-forge \
      xgboost lightgbm catboost \
      mlxtend \
      shap \
      uvicorn starlette aiohttp
