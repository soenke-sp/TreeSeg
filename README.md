# TreeSeg

A tool developed to automate the segmentation of individual trees. It utilizes ArcGIS Pro and Python and allows processing of UAV multispectral images with channels for RGB, near-infrared, and red edge. The tool provides selection among four tested models: Faster R-CNN, Mask R-CNN, TensorMask, and SAM.
For Faster R-CNN, Mask R-CNN, and TensorMask, the NDRE of the multispectral image is first calculated. Subsequently, instance segmentation is performed, and a shapefile containing the individual trees is generated. It should be noted that, due to the optimal hyperparameter configuration, the calculation using SAM may take more than a day.

## Installation

To run this project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/my-project.git`
2. Navigate to the project directory: `cd my-project`
3. Follow the installation instructions: `instructions.md`

## Usage

Run the project with the command `python main.py`. Additional options are available in the documentation.

## Contributing

Please read our [contribution guidelines](CONTRIBUTING.md) before submitting any changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, please contact me at [email@example.com](mailto:email@example.com).
