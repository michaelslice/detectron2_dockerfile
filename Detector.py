from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode, Visualizer 
from detectron2 import model_zoo
import cv2
import numpy as np

class Detector:
    def __init__(self, model_type = "OD"):
        '''
        __init__ Setup a model to determine the computational task
        
        model_type: Model to use, depending on model_type, we will load different model configurations and weights
        
        '''
        self.cfg = get_cfg()         # Store model settings, like model architecture, and weights
        self.model_type = model_type # Type of model to use
        
        # Object Detection
        if model_type == "OD":
            self.cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml"))
            self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml")
        # Instance segmentation
        elif model_type == "IS":
            self.cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
            self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")        
        # Keypoint Detection
        elif model_type == "KP":
            self.cfg.merge_from_file(model_zoo.get_config_file("COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml"))
            self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml")    
        # LVIS Instance Segmentation
        elif model_type == "LVIS":
            self.cfg.merge_from_file(model_zoo.get_config_file("LVISv0.5-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml"))
            self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("LVISv0.5-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml")    
        # Panoptic Segmentation
        elif model_type == "PS":
            self.cfg.merge_from_file(model_zoo.get_config_file("COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml"))
            self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml")                
        
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7 # Only predictions above 0.7 will be considered
        self.cfg.MODEL.DEVICE = "cuda"                   # Use cuda or cpu
        self.predictor = DefaultPredictor(self.cfg)      # Include default behavior for model loading, preprocessing, and operates on single image rather than batches
        
    def onImage(self, imagePath):
        '''
        onImage: Process a image using various computer vision models
        
        imagePath: The absolute path to the file you would like to use
        '''
        
        image = cv2.imread(imagePath)
        if self.model_type != "PS":
            # Use pre-trained model to make predictions on the current frame
            predictions = self.predictor(image)    
            
            # visualizer:                                      A utility to visualize the predictions on the image
            # image[:,:,::-1]:                                 Converts the image from BGR(OpenCV default) to RGB
            # MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]): Retrieves metadata for the dataset used to train the model.   
            # draw_instance_predictions:                       Draws the predicted instances(objects) on the image
            # predictions["instances"].to("cpu"):              Moves the predictions to the CPU for visualization 
            viz = Visualizer(image[:,:,::-1], metadata= MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]),
            
            # ColorMode.SEGMENTATION
            # ColorMode.IMAGE
            instance_mode= ColorMode.IMAGE)
            output = viz.draw_instance_predictions(predictions["instances"].to("cpu"))
        else:
            predictions, segmentInfo = self.predictor(image)["panoptic_seg"]
            viz = Visualizer(image[:,:,::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]))
            output = viz.draw_panoptic_seg_predictions(predictions.to("cpu"), segmentInfo)
        
        # Display the visualized predictions in a window 
        cv2.imshow("Result", output.get_image()[:,:,::-1])
        cv2.waitKey(0)
    
    def onVideo(self, videoPath):
        '''
        onVideo: Process a video using 
        
        imagePath: The absolute path to the file you would like to use
        '''
        
        # Initialize a video capture object, and check if open correctly
        cap = cv2.VideoCapture(videoPath)
        if(cap.isOpened() == False):
            print("Error, opening file")
            return
        
        # success: Boolean if frame was successfully
        # image: Frame of image from video
        (success, image) = cap.read()
        
        # Iterate as long as frames are read from the video
        while success:      
            # If model not Panoptic Segmentation
            if self.model_type != "PS":
                predictions = self.predictor(image)    
                viz = Visualizer(image[:,:,::-1], metadata= MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]),
                instance_mode= ColorMode.IMAGE)
                output = viz.draw_instance_predictions(predictions["instances"].to("cpu"))
            else:
                predictions, segmentInfo = self.predictor(image)["panoptic_seg"]
                
                # Visualizes the panoptic segmentation predictions on the image.
                viz = Visualizer(image[:,:,::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]))
                output = viz.draw_panoptic_seg_predictions(predictions.to("cpu"), segmentInfo)
            
            # Display the visualized predictions in a window 
            cv2.imshow("Result", output.get_image()[:,:,::-1])
            
            # If press q stop model and video processing
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            
            # Read the next frame from the video
            (success, image) = cap.read()
            
            
    def validateUser(self, videoPath):
        '''
        validateUser: Validate if a user sent a video of a person walking 
        
        imagePath: The absolute path to the file you would like to use
        '''
        
        cap = cv2.VideoCapture(videoPath)
        if(cap.isOpened() == False):
            print("Error, opening file")
            return
        
        (success, image) = cap.read()

        while success:      
            if self.model_type != "PS":
                predictions = self.predictor(image)
                viz = Visualizer(image[:,:,::-1], metadata= MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]),
                instance_mode= ColorMode.SEGMENTATION)                    
                output = viz.draw_instance_predictions(predictions["instances"].to("cpu"))
            else:
                predictions, segmentInfo = self.predictor(image)["panoptic_seg"]
                outputs = self.predictor(image)
                                
                # instances:              Detected objects in the frame
                # detected_class_indexes: Class indices of the detected objects
                # prediction_boxes:       Bounding box coordinates of the detected objects
                instances = outputs["instances"]
                detected_class_indexes = instances.pred_classes
                prediction_boxes = instances.pred_boxes
                
                # Retrieve the class names from metadata dataset
                metadata = MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0])
                class_catalog = metadata.thing_classes
                
                # Loop through the detected objects and check if a 
                # person is detected, if so break out of loop
                for idx, coordinates in enumerate(prediction_boxes):
                    class_index = detected_class_indexes[idx]
                    class_name = class_catalog[class_index]
                    
                    # If we detect a person the video is valid
                    if "person" in class_catalog[class_index]:
                        print("PERSON DETECTED")
                        # return
                    print(class_name, coordinates)
                
                viz = Visualizer(image[:,:,::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]))
                output = viz.draw_panoptic_seg_predictions(predictions.to("cpu"), segmentInfo)
            
            cv2.imshow("Result", output.get_image()[:,:,::-1])
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

            (success, image) = cap.read()