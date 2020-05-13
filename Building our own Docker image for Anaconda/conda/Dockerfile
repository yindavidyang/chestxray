FROM yinyang/cuda

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
   /bin/bash ~/miniconda.sh -b -p /opt/conda && \
   rm ~/miniconda.sh && \
   ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
   echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
   echo "conda activate base" >> ~/.bashrc

RUN /opt/conda/bin/conda install -y \
      jupyter \
      seaborn plotly \
      scikit-learn scikit-image \
      dask dask-image \
      beautifulsoup4

RUN /opt/conda/bin/conda install -yc conda-forge \
      xgboost lightgbm catboost \
      mlxtend \
      shap \
      uvicorn starlette aiohttp

CMD ["bash"]
