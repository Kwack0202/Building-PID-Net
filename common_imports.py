# ======================================================
# basic
import pandas as pd 
import numpy as np
import warnings

import random

import os
import glob
import shutil

from tqdm import tqdm

# ======================================================
# data file 
import json
from PIL import Image, ImageDraw
from collections import defaultdict
import cv2

import concurrent.futures

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# ======================================================
# torch, mmcv
import torch, torchvision

import mmcv

# 각 supercategory별로 색상 지정 (RGB 형태)
colors = {
    'background' : (0, 0, 0),
                 
    'roadlane': (255, 255, 255),         
         
    'guidance': (0, 128, 0),
    
    'direction': (255, 105, 180),              

    'etc': (128, 0, 128),
    
    'speed_restriction': (255, 0, 0)                              
}