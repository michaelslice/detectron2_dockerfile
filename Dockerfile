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
    libgl1 \
    ffmpeg \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.8 as the default Python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# Upgrade pip and install Python dependencies
RUN python3 -m pip install --upgrade pip && \
    pip3 install opencv-python && \
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu113 && \
    python3 -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

# Download the required models and configuration files
RUN mkdir -p /iGAIT-VIDEO-PRECHECK/
RUN wget -O /iGAIT-VIDEO-PRECHECK/panoptic_fpn_R_101_3x.yaml https://dl.fbaipublicfiles.com/detectron2/COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml
RUN wget -O /iGAIT-VIDEO-PRECHECK/model_final_cafdb1.pkl https://dl.fbaipublicfiles.com/detectron2/COCO-PanopticSegmentation/panoptic_fpn_R_101_3x/139514519/model_final_cafdb1.pkl

# Object Detection Model
RUN wget -O /iGAIT-VIDEO-PRECHECK/faster_rcnn_R_101_FPN_3x.yaml https://dl.fbaipublicfiles.com/detectron2/COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml
RUN wget -O /iGAIT-VIDEO-PRECHECK/faster_rcnn_R_101_FPN_3x_checkpoint.pkl https://dl.fbaipublicfiles.com/detectron2/COCO-Detection/faster_rcnn_R_101_FPN_3x.pkl

# Instance Segmentation Model
RUN wget -O /iGAIT-VIDEO-PRECHECK/mask_rcnn_R_50_FPN_3x.yaml https://dl.fbaipublicfiles.com/detectron2/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml
RUN wget -O /iGAIT-VIDEO-PRECHECK/mask_rcnn_R_50_FPN_3x_checkpoint.pkl https://dl.fbaipublicfiles.com/detectron2/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.pkl

# Keypoint Detection Model
RUN wget -O /iGAIT-VIDEO-PRECHECK/keypoint_rcnn_R_50_FPN_3x.yaml https://dl.fbaipublicfiles.com/detectron2/COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml
RUN wget -O /iGAIT-VIDEO-PRECHECK/keypoint_rcnn_R_50_FPN_3x_checkpoint.pkl https://dl.fbaipublicfiles.com/detectron2/COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.pkl

# LVIS Instance Segmentation Model
RUN wget -O /iGAIT-VIDEO-PRECHECK/mask_rcnn_X_101_32x8d_FPN_1x.yaml https://dl.fbaipublicfiles.com/detectron2/LVISv0.5-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml
RUN wget -O /iGAIT-VIDEO-PRECHECK/mask_rcnn_X_101_32x8d_FPN_1x_checkpoint.pkl https://dl.fbaipublicfiles.com/detectron2/LVISv0.5-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.pkl

# Set the working directory
WORKDIR /iGAIT-VIDEO-PRECHECK/

# Copy the rest of the application code
COPY . .

# Execute the script
CMD ["python3", "./validate_user.py"]