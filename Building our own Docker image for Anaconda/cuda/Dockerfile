FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y upgrade && apt-get install -y apt-utils

RUN apt-get install -y \
        net-tools iputils-ping \
        build-essential cmake git \
        curl wget \
        vim \
        zip p7zip-full p7zip-rar \
        imagemagick ffmpeg \
        libomp5

CMD ["bash"]
