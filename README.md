# TreeSeg

A tool for the segmentation of individual trees. It utilizes ArcGIS Pro and Python and allows processing of UAV multispectral images with channels for RGB, near-infrared, and red edge. The tool provides selection among four tested models: Faster R-CNN, Mask R-CNN, TensorMask, and SAM.

For Faster R-CNN, Mask R-CNN, and TensorMask, the NDRE of the multispectral image is first calculated. Subsequently, instance segmentation is performed, and a shapefile containing the individual trees is generated. It should be noted that, due to the optimal hyperparameter configuration, the calculation using SAM may take more than a day.

## Installation

To run this project, follow these steps:

1. Download the script tool file here.
2. Open the file in ArcGIS Pro.
3. Run the script tool and follow the instructions.

## Usage

1. Import the UAV multispectral image into ArcGIS Pro.
2. Select the desired model.
3. Run the script tool to perform the instance segmentation and generate the shapefile of individual trees.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, please contact me at [s41166332@gmail.com](mailto:s41166332@gmail.com).
