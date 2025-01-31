# iGAIT Video Check Notes & Design

### Goal: Train a computer vision model to detect a child walking, and validate front-facing and side-facing walking videos

### Data Collection & Validation
- The data our model will be trained on will be children walking, and the data we collect is front-facing and side-facing walking videos
- **Original Training Data**: Children walking videos
- **Masked Training Data**: We will need to mask the original training data. We do this because it allows for precision in training. It will help the model presisely learn and better detection accuracy.
### Original Data & Masked Version
![alt text](Examples\Images\Original_and_Masked.png)

---

### What Model Can Represent Object Detection? and Movement Overtime?
- **Faster R-CNN**: Is a object detection model that identifies objects in an image and draws bounding boxes arond them, while also classyfing what those objects are.  It’s a two-stage detector:
    - **Stage 1**: Proposes potential regions in the image that might contain objects. This is handled by the Region Proposal Network (RPN).
    - **Stage 2**: Uses these proposed regions to predict the class of the object and refines the bounding box to better match the object.
<br>

# The Architecture of Faster R-CNN

![alt text](Examples\Images\Faster-RCNN.png)

## Characteristics of Faster R-CNN

### Stage 1: Region Proposal Network (RPN)

**Backbone Network:**
- The image passes through a convolutional network (like ResNet or VGG16).
- This extracts important features from the image and creates a feature map.

**Anchors:**
- Anchors are boxes of different sizes and shapes placed over points on the feature map.
- Each anchor box represents a possible object location.
- At every point on the feature map, anchor boxes are generated with different sizes and aspect ratios.

**Classification of Anchors:**
- The RPN predicts whether each anchor box is background (no object) or foreground (contains an object).
- Positive (foreground) anchors: Boxes with high overlap with actual objects.
- Negative (background) anchors: Boxes with little or no overlap with objects.

**Bounding Box Refinement:**
- The RPN also refines the anchor boxes to better align them with the actual objects by predicting offsets (adjustments).

**Loss Functions:**
1. **Classification loss:** Helps the model decide if the anchor is background or foreground.
2. **Regression loss:** Helps adjust the anchor boxes to fit the objects more precisely.

---

### Stage 2: Object Classification and Box Refinement

**Region Proposals:**
- After RPN, we get region proposals (refined boxes that likely contain objects).

**Region of Interest Pooling:**
- The region proposals have different sizes, but the neural network needs fixed-size inputs.
- Region of Interest Pooling resizes all region proposals to a fixed size by dividing them into smaller regions and applying pooling, making them uniform.

**Object Classification:**
- Each region proposal is passed through a small network to predict the category (car, dog, etc.) of the object inside it.

**Bounding Box Refinement (Again):**
- The region proposals are refined again to better match the actual objects, using offsets.
- This uses regression loss to adjust the proposals.

**Multi-Task Learning:**
- The network in stage 2 learns both to predict object categories and refine bounding boxes at the same time.

### Inference (Testing/Prediction Time)

**Top Region Proposals:**
- During testing, the model generates a large number of region proposals, but only the top proposals (with the highest classification scores) are passed to the second stage.

**Final Predictions:**
- The second stage predicts the final categories and bounding boxes.

**Non-Max Suppression:**
- A technique called Non-Max Suppression is applied to remove duplicate or overlapping boxes, keeping only the best ones.

### Training

**Two Ways to Train:**
1. **Train in stages:**
   - First, train the region proposal network (RPN) and then the classifier and regressor.
2. **Train together:**
   - Train both stages at the same time (faster and more efficient).

---

# How Do We Handle Temporal Information (Movement Over Time) in a Video?

Using Faster R-CNN, we can detect objects in a frame (object detection). However, to understand movement over time, we need to look into **object tracking**. Object tracking involves following objects across frames using their **spatial** (position) and **temporal** (time-based) features.

## Object Tracking Process
Tracking is a two-step process:
1. **Detection and Localization**: 
   - Detect and localize objects in the frame using an object detector (e.g., YOLOv7, YOLOR, Faster R-CNN, etc.).
2. **Motion Prediction**:
   - Predict the future motion of the object using its past information (e.g., position, velocity) with a motion predictor.

## Types of Trackers
- **Single Object Tracker**: Tracks one object in the video.
- **Multiple Object Tracker**: Tracks multiple objects simultaneously.

---

# What is DeepSORT?

DeepSORT is a **Computer Vision Tracking Algorithm** used to track objects while assigning each tracked object a **unique ID**. It builds on the SORT (Simple Online and Realtime Tracking) algorithm but incorporates additional features to improve tracking accuracy.

![DeepSORT Overview](Examples\Images\DeepSORT_Algo.png)

---

# How Does DeepSORT Work?

DeepSORT extends the SORT algorithm by incorporating **appearance features** alongside motion-based tracking. Here’s how it works:

## Components of DeepSORT:
1. **Detection**:
   - Objects are detected in the frame using a detector like YOLOv5, YOLOv7, or Faster R-CNN.
   - These detections are passed to the next step.

2. **Estimation**:
   - The Kalman Filter predicts the position of each object in the next frame using a **Gaussian distribution** and a **constant velocity model**.
   - This step estimates the future location of the object based on its past motion.

3. **Data Association**:
   - A **cost matrix** is computed using the **Intersection-over-Union (IoU)** distance between:
     - Detected bounding boxes (from the current frame).
     - Predicted bounding boxes (from the Kalman Filter).
   - The Hungarian Algorithm is used to match detections to existing tracks efficiently.

4. **Creation and Deletion of Track Identities**:
   - When an object enters the frame, a **new unique ID** is assigned.
   - When an object leaves the frame, its ID is **destroyed**.

---

## Why DeepSORT?
- **SORT Limitations**: SORT relies only on motion information, which can lead to ID switches and tracking failures in complex scenarios (e.g., occlusions).
- **DeepSORT Improvements**: DeepSORT adds **appearance descriptors** (using a deep learning model) to distinguish objects based on their visual features, reducing ID switches and improving robustness.

---

## Key Takeaways:
- DeepSORT combines **motion-based tracking** (Kalman Filter) with **appearance-based tracking** (deep learning features).
- It is widely used in real-time applications like surveillance, sports analytics, and autonomous driving due to its accuracy and efficiency.

--- 

## Alternatives to Faster R-CNN for Video Detection
If Faster R-CNN is too slow or not suitable for your use case, consider these alternatives:

- **YOLO (You Only Look Once)**: Faster and more efficient for real-time video detection.
- **SSD (Single Shot Detector)**: Balances speed and accuracy.
- **EfficientDet**: A more efficient and scalable object detection model.
- **Transformer-based Detectors (e.g., DETR)**: Newer architectures with strong performance.

--- 

## Examples Photos
## Faster R-CNN Object Detection
![alt text](Examples\Images\FasterRCNN_Detection.png)
## DeepSORT Motion Detection
![alt text](Examples\Images\DeepSORT_Detection.png)

## YouTube Video
Video of DeepSORT in action [Link](https://alex.bewley.ai/misc/SORT-MOT17-06-FRCNN.webm)

## Example Workflow
**Input Video**:
- The video is fed into the system frame by frame.

**Detection**:
- Faster R-CNN detects objects in each frame and classifies them (e.g., "child" or "adult").

**Tracking**:
- DeepSORT tracks the detected child across frames and estimates their movement.

**Analysis**:
- If a child is detected and their movement suggests walking, the system outputs "yes." Otherwise, it outputs "no."

**Output**:
- The final result is a simple "yes" or "no" indicating whether a child is walking in the video.