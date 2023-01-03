"""
The constants module: Application constants.

Provides global constants to be used throughout the application.
"""

from os import getcwd
from os.path import join

DATA_DIR = join(getcwd(), 'Data')
SNOMED_DIR = join(DATA_DIR, 'Snomed')
SNOMED_CSV = 'Snomed.csv'