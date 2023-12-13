from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import numpy as np
import os

#SAM model type:
checkpoint_path = "checkpoint/sam_vit_h_4b8939.pth"

def show_anns(anns):
    global img
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask

assets = os.listdir("input_images/")

for raster in assets:
    input_img = rasterio.open("input_images/" + raster)
    
    band_1 = input_img.read(3)*255.0/input_img.read(3).max() 
    band_2 = input_img.read(2)*255.0/input_img.read(2).max() 
    band_3 = input_img.read(1)*255.0/input_img.read(1).max() 
    
    rgb_img = np.uint8(np.dstack((band_1,band_2,band_3)))
    
    sam = sam_model_registry[model_type](checkpoint=checkpoint_path)
    
    mask_generator = SamAutomaticMaskGenerator(
        model=sam,
        points_per_side=32,
        pred_iou_thresh=0.5,
        stability_score_thresh=0.5,
        stability_score_offset=1,
        box_nms_thresh=1,
        crop_n_layers=5,
        crop_overlap_ratio=0.5,
        crop_n_points_downscale_factor=2,
        min_mask_region_area=1000
            )
    
    masks = mask_generator.generate(rgb_img)
    
    index = 0
    while index != len(masks):
        if 15000 <= masks[index]["area"] <= 700000:
            index += 1
        else:
            del masks[index]
    
    result_mask = np.full(np.shape(masks[0]["segmentation"]), False)
    for index in masks:
        result_mask = np.logical_or(result_mask, index["segmentation"])

    # Generate images from masks:
    image_array = np.where(predict == 1, 255, result_mask)
    image_array = np.stack([image_array, image_array, image_array], axis=0).astype(np.uint8)
    image = cv2.cvtColor(image_array.transpose(1, 2, 0), cv2.COLOR_RGB2BGR)
    cv2.imwrite("output_images/" + image_in[:-4] + '_mask.jpg', image)  
