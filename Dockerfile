# Base image with CUDA 11.3.1 and cuDNN 8
FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

# Install system dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    git \
    python3.8 \
    python3.8-dev \
    python3.8-distutils \
    python3-pip \
    libgl1 \
    ffmpeg \
    wget \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libqt5x11extras5 \
    g++ \ 
    gcc \ 
    cmake \
    libgtk2.0-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.8 as the default Python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# Upgrade pip and install Python dependencies
RUN python3 -m pip install --upgrade pip && \
    pip3 install opencv-python-headless && \
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu113 && \
    python3 -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

# Create data directory
RUN mkdir -p data
COPY ./data data

# Download the model file and set permissions
RUN wget https://dl.fbaipublicfiles.com/detectron2/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl -O model_final_cafdb1.pkl && \
    chmod 644 model_final_cafdb1.pkl

# Copy the rest of the application code
COPY . .

# Set proper permissions for the data directory
RUN chmod -R 755 data