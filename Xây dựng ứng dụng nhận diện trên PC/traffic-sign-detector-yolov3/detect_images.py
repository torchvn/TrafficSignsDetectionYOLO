import os
import numpy as np
import cv2
from yolo_utils import *

# print('OpenCV version : ', cv2. __version__)
# print(cv2.cuda.getCudaEnabledDeviceCount())


# test our function read_classes
img_file = './data/yolo.names'
classNames = read_classes(img_file)
# print("Classes' names :\n", classNames)


# load the model config and weights
modelConfig_path = './cfg/yolov3-43c-86000-max-steps.cfg'
modelWeights_path = './weights/yolov3-43c-86000-max-steps_best.weights'

# read the model cfg and weights with the cv2 DNN module
neural_net = cv2.dnn.readNetFromDarknet(modelConfig_path, modelWeights_path)
# # set the preferable Backend to GPU
# neural_net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# neural_net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)



# defining the input frame resolution for the neural network to process
network = neural_net
height, width = 416,416

# confidence and non-max suppression threshold for this YoloV3 version
confidenceThreshold = 0.5
nmsThreshold = 0.2

# load the image
img = load_image('/xanh06.jpg')

# using convert_to_blob function : 
outputs = convert_to_blob(img, network, height, width)    
# apply object detection on the video file
bounding_boxes, class_objects, confidence_probs = object_detection(outputs, img, confidenceThreshold)   
# perform non-max suppression
indices = nms_bbox(bounding_boxes, confidence_probs, confidenceThreshold, nmsThreshold)
# draw the boxes
box_drawing(img, indices, bounding_boxes, class_objects, confidence_probs, classNames, color=(255,0,0), thickness=2)

# to save the detected image
img_save = cv2.imwrite('./results/images/yolov4res11.jpg', img)

cv2.imshow('Object detection in images', img)
cv2.waitKey()
cv2.destroyAllWindows()