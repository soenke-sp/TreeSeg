# Changelog

All notable changes to this project will be documented in this file.

## [1.0] - 6-26-2024
1. **Added Band Order Input Parameter**:
   - Introduced a new input parameter to allow users to specify the order of bands (Red, Green, Blue, Near Infrared, Red Edge) using a comma-separated list of indices. This enables automatic band assignment based on user-defined order.

2. **Replaced OpenCV and Rasterio with arcpy and Pillow**:
   - Updated the code to use `arcpy` and `Pillow` instead of `OpenCV` and `Rasterio` to ensure compatibility with the default environment of ArcGIS Pro. This change ensures that dependencies are met without requiring additional installations.
