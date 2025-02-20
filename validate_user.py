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
    valid_options = ("OD", "IS", "KP", "LVIS", "PS")
    model = input("Which model would you like to use?, enter OD, IS, KP, LVIS, PS: ").strip().upper()
    
    # Validate input
    if model in valid_options:

        option = input("Would you like to use photo or video?, enter 1(photo), 2(video): ").strip()
        
        # Image
        if int(option) == 1:
            print("Processing Image")
            detector = Detector(model_type=model)    
            
            # Process comand line arg
            video_path = sys.argv[1]
                
            # Check if file exists
            if not os.path.exists(sys.argv[1]):
                print(f"Error: Video file not found at {sys.argv[1]}")
                print("Contents of data directory:")
                print(os.listdir('/data'))
                return

            # Run model
            result = detector.onImage(sys.argv[1])

        # Video            
        elif int(option) == 2:
            print("Processing Video")
            # model_type="PS" is best option
            detector = Detector(model_type=model)    
            
            # Process comand line arg
            video_path = sys.argv[1]
                
            # Check if file exists
            if not os.path.exists(sys.argv[1]):
                print(f"Error: Video file not found at {sys.argv[1]}")
                print("Contents of data directory:")
                print(os.listdir('/data'))
                return

            # Run video
            result = detector.onVideo(sys.argv[1])
        
    else:
        print("Error invalid option entered.")

if __name__ == "__main__":
    main()