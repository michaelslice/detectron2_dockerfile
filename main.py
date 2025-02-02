from Detector import *

# OD
# IS
# KP, pose mapping
# LVIS, trained on more rare item dataset
# PS
detector = Detector(model_type="PS")
detector.onVideo("C:/Users/User/Desktop/igait-video-precheck/Examples/Detectron2_Test/data/5.MOV")