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

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Set the working directory
WORKDIR /iGAIT-VIDEO-PRECHECK/Examples/Detectron2_Test

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install opencv-python
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu113

# Install Detectron2
RUN python3 -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

# Download repo
RUN git clone 'https://github.com/facebookresearch/detectron2.git' .

# Copy the rest of the application code
COPY . .

# Set the working directory to the Detectron2 test directory
WORKDIR /iGAIT-VIDEO-PRECHECK/Examples/Detectron2_Test

# Execute the script
CMD ["python3", "./validate_user.py"]