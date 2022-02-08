# import useful libraries
import os
import numpy as np
import cv2
from yolo_utils import *


# load the obj/classes names
obj_file = './data/yolo.names'
classNames = read_classes(obj_file)
print("Classes' names :\n", classNames)


# load the model config and weights
modelConfig_path = './cfg/yolov3-43c-86000-max-steps.cfg'
modelWeights_path = './weights/yolov3-43c-86000-max-steps_best.weights'

# read the model cfg and weights with the cv2 DNN module
neural_net = cv2.dnn.readNetFromDarknet(modelConfig_path, modelWeights_path)




# confidence and non-max suppression threshold for this YoloV3 version
confidenceThreshold = 0.5
nmsThreshold = 0.1

# defining the input frame resolution for the neural network to process
# we can decrease the height and width but the minimum is 320x320.
network = neural_net
height, width = 320, 320

# load the video
cap_video = load_video('/test2.mp4')

# save the video with object detections
frame_width = int(cap_video.get(3))
frame_height = int(cap_video.get(4))
# video_frames_save = cv2.VideoWriter('./results/videos/resultvidcolab6.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 60, (frame_width,frame_height))

while cap_video.isOpened():
    success, video_frames = cap_video.read()
    # if 'video_frames' is read correctly 'success' is True
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
        
    # using convert_to_blob function : 
    outputs = convert_to_blob(video_frames, network, height, width)    
    # apply object detection on the video file
    bounding_boxes, class_objects, confidence_probs = object_detection(outputs, video_frames, confidenceThreshold)   
    # perform non-max suppression
    indices = nms_bbox(bounding_boxes, confidence_probs, confidenceThreshold, nmsThreshold)
    # draw the boxes
    box_drawing(video_frames, indices, bounding_boxes, class_objects, confidence_probs, classNames, color=(0,255,255), thickness=2)
    # save the video
    # video_frames_save.write(video_frames)
    
    cv2.imshow('Object Detection in videos', video_frames)         
    
    if cv2.waitKey(1) == ord('q'):
        break
        
cap_video.release()
cv2.destroyAllWindows()
