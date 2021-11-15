#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import cv2
from google.colab.patches import cv2_imshow
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    resized_Image = cv2.resize(X, dsize=resize, interpolation=cv2.INTER_CUBIC)
    cv2_imshow(resized_Image)
pass

