# Base image with CUDA 11.3.1 and cuDNN 8
FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    python3.8 \
    python3.8-dev \
    python3.8-distutils \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.8 as the default Python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# Upgrade pip and install Python dependencies
RUN python3 -m pip install --upgrade pip && \
    pip3 install opencv-python torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu113 && \
    python3 -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

# Set the working directory
WORKDIR /iGAIT-VIDEO-PRECHECK/Examples/Detectron2_Test

# Copy the requirements file and install dependencies
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Execute the script
CMD ["python3", "./validate_user.py"]