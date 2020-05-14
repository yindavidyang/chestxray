FROM yinyang/conda

RUN /opt/conda/bin/conda install -y \
      cudatoolkit=10.1 \
      cudnn

RUN /opt/conda/bin/conda install -yc pytorch pytorch torchvision

RUN /opt/conda/bin/conda install -yc fastai fastai

RUN /opt/conda/bin/conda uninstall -y --force pillow pil jpeg libtiff libjpeg-turbo
RUN /opt/conda/bin/conda install -yc conda-forge libjpeg-turbo
RUN /opt/conda/bin/conda uninstall -y --force pillow
RUN CFLAGS="${CFLAGS} -mavx2" /opt/conda/bin/pip install --upgrade --no-cache-dir --force-reinstall --no-binary :all: --compile pillow-simd

RUN /opt/conda/bin/pip install efficientnet-pytorch object-detection-fastai

CMD ["bash"]
