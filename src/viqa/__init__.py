"""
vIQA (volumetric Image Quality Assessment) is a Python package for the assessment of volumetric image quality.
It provides a set of metrics to assess the quality of volumetric images. The package can be used for 2D and 3D images.
"""

__version__ = "0.8.2dev0"
__author__ = "Lukas Behammer"

from .fr_metrics import *
from .nr_metrics import *
