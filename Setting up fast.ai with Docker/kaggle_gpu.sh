docker run --rm -it \
        --gpus all \
        --shm-size=1024m \
        -p 8888:8888 \
        -v /media/yyang/data:/data \
        kaggle/python-gpu-build \
        bash
