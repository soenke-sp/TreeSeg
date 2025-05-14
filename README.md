⚠️ **This project is no longer maintained.**

The TreeSeg toolbox is outdated and no longer actively supported. While the code remains available for reference, it may not be compatible with the latest versions of ArcGIS Pro or Python environments. Use at your own risk.


# TreeSeg

A tool for the segmentation of individual trees. It utilizes ArcGIS Pro and Python and allows processing of UAV multispectral images with channels for RGB, near-infrared, and red edge. The tool provides selection among four tested models: Faster R-CNN, Mask R-CNN, TensorMask, and SAM.

For Faster R-CNN, Mask R-CNN, and TensorMask, the NDRE (Normalized Difference Red Edge Index) of the multispectral image is first calculated. Subsequently, instance segmentation is performed, and a shapefile containing the individual trees is generated. It should be noted that, due to the optimal hyperparameter configuration, the calculation using SAM may take more than a day.


![Tree Segmentation Example](img/example.PNG)

## Installation

To run this project, follow these steps:

1. Download the toolbox file [here](https://github.com/soenke-sp/TreeSeg/raw/main/toolbox/TreeSegV1.0.atbx).
2. Open **TreeSegV1.0.atbx** in ArcGIS Pro. See [Connect to a toolbox](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-a-toolbox.htm) for more information.
3. Run the script tool and follow the instructions.

## Usage

1. Import the UAV multispectral image (B, G, R, NIR, RE) into ArcGIS Pro.
2. Select the desired model.
3. Run the script tool to perform the instance segmentation and generate the shapefile of individual trees.  
*Upon first execution of the tool, automatic installation of the required dependencies will occur. This process may take 20 minutes or longer, depending on your internet connection and system performance.*

## Sample Dataset

To test or explore the tool with example data, you can download a sample UAV multispectral dataset here:  
[Download Sample Dataset](**INSERT-YOUR-LINK-HERE**)

This dataset includes:

- Multispectral UAV imagery (RGB, NIR, RE)
- Reference shapefiles of individual trees for validation or comparison

## Known Issues

### ⚠️ Python Imaging Library (PIL) Error

Some users have encountered the following error when running the tool:

AttributeError: module 'PIL' has no attribute 'Image'

This error typically occurs when PIL is imported incorrectly. To fix it:

1. Ensure you import the module correctly:  
   from PIL import Image

2. Make sure that the Pillow library (a maintained fork of PIL) is installed and up to date:  
   pip install --upgrade pillow

3. If the issue persists, refer to this helpful StackOverflow thread:  
   https://stackoverflow.com/questions/11911480/python-pil-has-no-attribute-image

## Model Checkpoints
The tool automatically downloads the required model checkpoints. For reference, the checkpoints can be found at the following links:

- **Faster R-CNN Checkpoint:** [Download](https://drive.google.com/file/d/10PO1XyerhIF8UV9DqO1B04AntQLI8R2E/view?usp=drive_link)
- **Mask R-CNN Checkpoint:** [Download](https://drive.google.com/file/d/1RkKmjvdPF53ebsneKzTk6H8s5AnfQQj3/view?usp=drive_link)
- **TensorMask Checkpoint:** [Download](https://drive.google.com/file/d/1FbUYydl0aXa5xQQ7c1wlmH9ZobPE4Ygh/view?usp=drive_link)


## Reference
For more detailed information, please refer to the related paper: [Link to Paper](https://www.mdpi.com/2072-4292/16/19/3660).

## License

This project is licensed under the [License](LICENSE).

## Contact

For questions or feedback, please contact me at [s41166332@gmail.com](mailto:s41166332@gmail.com).
