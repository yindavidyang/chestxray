#!/bin/bash

~/conda/bin/conda install -y \
      cudatoolkit=10.1 \
      cudnn

~/conda/bin/conda install -yc pytorch pytorch torchvision

~/conda/bin/conda install -yc fastai fastai
