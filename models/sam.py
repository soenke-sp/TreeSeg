# Import libaries:
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import numpy as np
import os
import cv2

# Load pre-trained weights for the model:
checkpoint_path = "sam_vit_h_4b8939.pth"

# Select SAM model:
model_type = "default"

# Generate annotations from images:
def show_anns(anns):
    global img
    if len(anns) == 0:
        return

    # Sort annotations by area in descending order:
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0

    # Generate and display masks with random colors:
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask

# List input images:
images = os.listdir("input_images/")

for img in images:

    # Read the input image:
    image = cv2.imread("input_images/" + img)

    # Initialize SAM model:
    sam = sam_model_registry[model_type](checkpoint=checkpoint_path)

    # Initialize mask generator with specified parameter:
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

    # Generate masks for the input image:
    masks = mask_generator.generate(image)

    # Filter masks based on area criteria:
    index = 0
    while index != len(masks):
        if 15000 <= masks[index]["area"] <= 700000:
            index += 1
        else:
            del masks[index]

    # Create a result mask by combining individual masks:
    result_mask = np.full(np.shape(masks[0]["segmentation"]), False)
    for index in masks:
        result_mask = np.logical_or(result_mask, index["segmentation"])

    # Convert result mask to uint8 format and save the output image:
    result_mask = np.uint8(255 * result_mask)
    cv2.imwrite("output_images/fertig.jpg", result_mask) 
