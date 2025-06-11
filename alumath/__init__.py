"""
Alumath - A simple matrix calculator library
"""

from .matrix import Matrix
from .operations import multiply_matrices, add_matrices, subtract_matrices

__version__ = "0.1.0"
__author__ = "Terry Manzi"
__email__ = "m.terry@alustudent.com"

__all__ = [
    "Matrix",
    "multiply_matrices", 
    "add_matrices",
    "subtract_matrices"
]