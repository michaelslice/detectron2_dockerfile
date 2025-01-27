Topic 1: Precheck user-submitted videos before gait analysis 

If a user accidentally (or intentionally) submits a video that is not a child walking, we want to detect it and stop the video analysis. For example, we won’t run OpenPose and the subsequent ML model. 

Method: There may exist software (or by combining multiple tools) that can detect the content of (simple) videos, and summarize it in a classifiable way. Just like image classification, there might be a method to tell if a video is about a child (or a person) walking back and forth, or about a dog running in a park, or about a wildfire, or simply “not a child walking”. 

Extension: If this is successful, maybe we can have a method to precheck if the user-submitted videos are compliant with expectation. For example, if the video only captures the right half of the child’ s body, then we stop the analysis and issue a message asking for resubmission. 

# How to Use
- Create a virtual environment ` python -m venv .env`
- Activate environment on windows `.myenv\Scripts\activate`
# Update your Packages
- `pip freeze > requirements.txt`
- `pip install -r ./requirements.txt`
