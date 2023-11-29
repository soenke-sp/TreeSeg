import torch, detectron2
import os
import sys
import numpy as np
import json, cv2, random, statistics
import matplotlib.pyplot as plt
import pandas as pd
import torch
import os

from detectron2.utils.logger import setup_logger
setup_logger()
from detectron2.data.datasets import register_coco_instances
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.config import CfgNode as CN

from detectron2.engine import DefaultTrainer
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader

os.environ["CUDA_VISIBLE_DEVICES"]="1"
