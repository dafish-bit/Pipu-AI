from imageai.Detection import ObjectDetection
import pygame
import cv2
# Instantiating the object detection class
detector = ObjectDetection()

# Setting a path to the YOLOv3 model
model_path = "yolov3.pt"

# Installing the YOLOv3 model and setting a path to the weights file
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)

# Loading the model
detector.loadModel()
print(detector.CustomObjects())
