"""`Horus.py` is the main program for the Horus project.
The Horus project utilizes convoluted neural networks for predicting the times of sunrise and sunset.

@author: nrosenthal
@version: 1.0
@since: 2024-11-02
"""

import numpy as np;
from datetime import datetime;
from datetime import timedelta;
import math;
import random;

import torch;
import torch.nn as nn;
import torch.nn.functional as F;

from torch.utils.data import DataLoader;
from torchvision import datasets;
from torchvision.transforms import ToTensor;


class Horus(nn.Module):
    def __init__(self):
        super(Horus, self).__init__();
        


def main() -> None:
    device = "cuda" if torch.cuda.is_available() else "cpu";
    print(f"PROJECT HORUS\nUsing {device} device");

    # Download training data from open datasets.
    training_data = datasets.FashionMNIST(

if __name__ == '__main__':
    main();
    exit (0);