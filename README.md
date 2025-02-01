# iGAIT ASD - Video Precheck

## Objective: Precheck user-submitted videos before gait analysis 

- If a user accidentally (or intentionally) submits a video that is not a child walking, we want to detect it and stop the video analysis. For example, we won’t run OpenPose and the subsequent ML model. 
- Method: There may exist software (or by combining multiple tools) that can detect the content of (simple) videos, and summarize it in a classifiable way. Just like image classification, there might be a method to tell if a video is about a child (or a person) walking back and forth, or about a dog running in a park, or about a wildfire, or simply “not a child walking”. 
- Extension: If this is successful, maybe we can have a method to precheck if the user-submitted videos are compliant with expectation. For example, if the video only captures the right half of the child’ s body, then we stop the analysis and issue a message asking for resubmission. 

## Prerequisites(Windows)
You need to make sure to download and follow all steps correctly, because the version Python packages Detectron2 uses, are only compatible with certain versions of CUDA. And Visual Studio 2017's MSVC Compiler is what is used to compile the CUDA C++ code.
- Download Python 3.8 [Link](https://www.python.org/downloads/release/python-380/)
- Download CUDA 11.3 [Link](https://developer.nvidia.com/cuda-11.3.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)
- Download Visual Studio 2017 [Link](https://quasar.ugent.be/files/doc/cuda-msvc-compatibility.html) 
## Download Repo and Requirements
- Download Repo: `git clone https://github.com/michaelslice/igait-video-precheck.git`
- Navigate to directory: `cd igait-video-precheck/Examples/Detectron2_test`
- Create a Virtual Environment for Python 3.8, your directory may be different: `C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe -m venv .env`
- Activate Environment: `.myenv\Scripts\activate`
- Download Requirements: `pip install -r requirements.txt`

## Run Models
- To run Detection model: `./main.py`

## Prerequisites(Linux) TODO

## Useful Resources
- Detectron2 GitHub [Link](https://github.com/facebookresearch/Detectron2)
