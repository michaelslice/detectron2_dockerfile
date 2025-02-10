from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode, Visualizer 
from detectron2 import model_zoo
import os 
import sys
import cv2
import numpy as np
from Detector import *

def main():
    print("Starting video validation...")
    
    # Create detector object
    detector = Detector(model_type="PS")
    
    # Process comand line arg
    video_path = sys.argv[1]
        
    # Check if file exists
    if not os.path.exists(sys.argv[1]):
        print(f"Error: Video file not found at {sys.argv[1]}")
        print("Contents of data directory:")
        print(os.listdir('/iGAIT-VIDEO-PRECHECK/data'))
        return
    
    # Validate the video, for person detection
    result = detector.validateUser(sys.argv[1])
    
    if result:
        print("Video validation completed successfully")
        print("Output frames have been saved to the output directory")
    else:
        print("Video validation failed")

if __name__ == "__main__":
    main()