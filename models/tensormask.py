# Import libaries:
import torch
import detectron2
import cv2
import os
import numpy as np

# Import logger setup function from Detectron2:
from detectron2.utils.logger import setup_logger

# Import relevant modules from Detectron2:
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg

# Set up Detectron2 logger:
setup_logger()
cfg = get_cfg()

# Select Tensormask model:
model_type = "COCO-InstanceSegmentation/tensormask_R_50_FPN_6x.yaml"
cfg.merge_from_file(model_zoo.get_config_file(model_type))

# Configure the hyperparameter:
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 2
cfg.MODEL.MASK_ON = True
cfg.SOLVER.MAX_ITER = 40000
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 1024
cfg.SOLVER.BASE_LR = 0.001
cfg.SOLVER.GAMMA = 0.01
cfg.SOLVER.WEIGHT_DECAY = 0.01
cfg.SOLVER.NESTEROV = True
cfg.SOLVER.MOMENTUM = 0.85
cfg.SOLVER.WEIGHT_DECAY_NORM = 0.05
cfg.SOLVER.BIAS_LR_FACTOR = 0.5
cfg.SOLVER.WEIGHT_DECAY_BIAS = 0.005
cfg.SOLVER.NUM_DECAYS = 5
cfg.SOLVER.WARMUP_FACTOR = 0.05
cfg.SOLVER.WARMUP_METHOD = "linear"

# Load pre-trained weights for the model:
cfg.MODEL.WEIGHTS = "tensormask_cp.pth"

# Set the threshold for the prediction:
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7

# Create predictor:
predictor = DefaultPredictor(cfg)

# Perform the prediction on images:
for image_in in os.listdir("input_images/"):
    
    # Load image and perform prediction:
    pred_img = cv2.imread("input_images/"+ image_in)
    outputs = predictor(pred_img)

    # Prepare predicted masks:
    masks = outputs["instances"].pred_masks.cpu().numpy()
    predict = np.zeros((np.shape(masks)[1],np.shape(masks)[2]))
    
    # Delete too big masks:
    i= 0
    while i != np.shape(masks)[0]:
        if np.count_nonzero(masks[i]) <= 150000:
            predict = np.where(predict != 0, 1,masks[i])
        i += 1
    
    # Generate images from masks:
    image_array = np.where(predict == 1, 255, predict)
    image_array = np.stack([image_array, image_array, image_array], axis=0).astype(np.uint8)
    image = cv2.cvtColor(image_array.transpose(1, 2, 0), cv2.COLOR_RGB2BGR)
    cv2.imwrite("output_images/" + image_in[:-4] + '_mask.jpg', image)  
