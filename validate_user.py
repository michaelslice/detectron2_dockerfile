from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode, Visualizer 
from detectron2 import model_zoo
import os 
import cv2
import numpy as np
from Detector import *

# For production script, probably will add file name as a command line arguement to run script
def main():
    detector = Detector(model_type="PS")
    detector.validateUser("C:/Users/User/Desktop/igait-video-precheck/data/5.MOV")

if __name__ == "__main__":
    main()