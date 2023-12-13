from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import numpy as np
import matplotlib.pyplot as plt
import os
import rasterio
import arcpy

#SAM model type:
checkpoint_path = "checkpoint/sam_vit_h_4b8939.pth"

#GPU number:
#device = "cuda:1"

#Hyperparameter
model_type = "default"

points_per_side = 32 #number of points to be sampled along one side of the image

pred_iou_thresh = 0.5 #filtering threshold in [0,1], using the model's predicted mask quality

stability_score_thresh=0.5 #filtering threshold in [0,1], using the stability of the mask under
                            #changes to the cutoff used to binarize the model's mask predictions
    
stability_score_offset = 1 #amount to shift the cutoff when calculated the stability score

box_nms_thresh = 1 #box IoU cutoff used by non-maximal suppression to filter duplicate masks

crop_n_layers=5 

crop_overlap_ratio = 0.5

crop_n_points_downscale_factor=2 #Quelle:https://replicate.com/pablodawson/segment-anything-automatic
                                 #Umformulieren!!!!!
min_mask_region_area=1000

assets = os.listdir("#input/")

#To visualize masks, copied from github/facebookresearch/segment-anything:
def show_anns(anns):
    global img
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    #ax = plt.gca()
    #ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
    #ax.imshow(img)

for raster in assets:
    #Test
    #rgb_img = cv2.imread("assets/" + raster) 
    
    #Input raster:
    input_img = rasterio.open("#input/" + raster)
    
    #Normalize rgb-bands between 0 and 255:
    band_1 = input_img.read(3)*255.0/input_img.read(3).max() 
    band_2 = input_img.read(2)*255.0/input_img.read(2).max() 
    band_3 = input_img.read(1)*255.0/input_img.read(1).max() 
    
    #Create image from rgb-bands:
    rgb_img = np.uint8(np.dstack((band_1,band_2,band_3)))
    
    #Create SAM-model, copied from github/facebookresearch/segment-anything:
    sam = sam_model_registry[model_type](checkpoint=checkpoint_path)
    
    #Set GPU:
    #sam.to(device=device)
    
    #Set Hyperparameter:
    mask_generator = SamAutomaticMaskGenerator(
        model=sam,
        points_per_side=points_per_side,
        pred_iou_thresh=pred_iou_thresh,
        stability_score_thresh=stability_score_thresh,
        stability_score_offset=stability_score_offset,
        box_nms_thresh=box_nms_thresh,
        crop_n_layers=crop_n_layers,
        crop_overlap_ratio=crop_overlap_ratio,
        crop_n_points_downscale_factor=crop_n_points_downscale_factor,
        min_mask_region_area=min_mask_region_area
            )
    
    #Generate segmenation masks:
    masks = mask_generator.generate(rgb_img)
    
    #Delete to small or to big segmentation masks:
    index = 0
    while index != len(masks):
        if 15000 <= masks[index]["area"] <= 700000:
            index += 1
        else:
            del masks[index]
    
    #Create segmentation mask from results:
    result_mask = np.full(np.shape(masks[0]["segmentation"]), False)
    for index in masks:
        result_mask = np.logical_or(result_mask, index["segmentation"])
