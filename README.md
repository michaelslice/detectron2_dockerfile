# iGAIT ASD - Video Precheck

## Objective: Precheck user-submitted videos before gait analysis 

- If a user accidentally (or intentionally) submits a video that is not a child walking, we want to detect it and stop the video analysis. For example, we won’t run OpenPose and the subsequent ML model. 
- Method: There may exist software (or by combining multiple tools) that can detect the content of (simple) videos, and summarize it in a classifiable way. Just like image classification, there might be a method to tell if a video is about a child (or a person) walking back and forth, or about a dog running in a park, or about a wildfire, or simply “not a child walking”. 
- Extension: If this is successful, maybe we can have a method to precheck if the user-submitted videos are compliant with expectation. For example, if the video only captures the right half of the child’ s body, then we stop the analysis and issue a message asking for resubmission. 

# Prerequisites(Windows)
- Download CUDA 12.8 [Download CUDA](https://developer.nvidia.com/cuda-downloads)
- Download pyTorch with CUDA support , to ensure GPU use <br> `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`


# How to Use
- git clone `https://github.com/michaelslice/igait-video-precheck.git`
- Create a virtual environment ` python -m venv .env`
- Activate environment on windows `.myenv\Scripts\activate`
# Update your Packages
- `pip freeze > requirements.txt`
- `pip install -r ./requirements.txt`
## Technologies Used
- Python
- PyTorch (with TorchVision or Detectron2)

## Useful Resources
- PyTorch Vision GitHub [Link](https://github.com/pytorch/vision)
