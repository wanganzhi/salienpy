#!/usr/bin/env python2
import cv2
import numpy as np

def signature_saliency(img):
    """
    Signature Saliency.


    X. Hou, J. Harel, and C. Koch, "Image Signature: Highlighting Sparse Salient
    Regions." IEEE Trans. Pattern Anal. Mach. Intell. 34(1): 194-201 (2012)
    """
    img = img/255.0
    sal = []
    for c in range(img.shape[2]):
        channel = img[:,:,c].astype(np.dtype('float32'))
        channel_dct = np.sign(cv2.dct(channel))
        s = cv2.idct(channel_dct)
        s = np.multiply(s,s)
        sal.append(s)
    sal = sum(sal)/3.0
    sal = sal - sal.min()
    sal = 255 * ( sal / sal.max())
    return sal