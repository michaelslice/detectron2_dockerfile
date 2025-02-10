# Detectron2 Dockerfile

## Objective  
Precheck user-submitted videos before gait analysis to ensure they feature a child walking. If not, analysis is halted.  

## Method  
We explore software to classify video content, similar to image classification, to detect if a video shows a child walking or irrelevant content (e.g., a dog running, wildfire, etc.). Future enhancements may verify video quality (e.g., ensuring full-body visibility).  

## Prerequisites  
- Install [Docker](https://www.docker.com/).  

## Usage  

### Pull the image 
```
docker pull ghcr.io/michaelslice/igait-detectron2:latest
```
### Run the image
- `docker run`: Runs a new container
- `--gpus all`: Run using gpus
- `-v /path_to_video_file:/iGAIT-VIDEO-PRECHECK/data`: Maps the local folder containing video files to the container’s directory
- `ghcr.io/michaelslice/igait-detectron2:latest`: The docker image to run
- `"/iGAIT-VIDEO-PRECHECK/path_to_your_data/YOUR_VIDEO.MOV"`: The video file to be analyzed
```
docker run --gpus all -v /path_to_video_file:/iGAIT-VIDEO-PRECHECK/data ghcr.io/michaelslice/igait-detectron2:latest "/iGAIT-VIDEO-PRECHECK/data/5.MOV"
```

### Example Usage on Windows
```
docker run --gpus all -v C:/Users/User/Desktop/igait-video-precheck/data:/iGAIT-VIDEO-PRECHECK/data ghcr.io/michaelslice/igait-detectron2:latest "/iGAIT-VIDEO-PRECHECK/data/5.MOV"
```

## Resources  
- [Detectron2 GitHub](https://github.com/facebookresearch/Detectron2)  
- [Detectron2 Model Zoo](https://github.com/facebookresearch/detectron2/blob/main/MODEL_ZOO.md)  
