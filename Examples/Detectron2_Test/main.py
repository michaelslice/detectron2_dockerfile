from Detector import *

# OD
# IS
# KP, pose mapping
# LVIS, trained on more rare item dataset
# PS
detector = Detector(model_type="PS")
# For some reason it only works with absolute path on windows...
# detector.onImage("C:/Users/User/Desktop/igait-video-precheck/Examples/Detectron2_Test/data/1.jpg")
# detector.onImage("C:/Users/User/Desktop/igait-video-precheck/Examples/Detectron2_Test/data/2.jpg")
# detector.onVideo("C:/Users/User/Desktop/igait-video-precheck/Examples/Detectron2_Test/data/3.MOV")
detector.onVideo("C:/Users/User/Desktop/igait-video-precheck/Examples/Detectron2_Test/data/5.MOV")