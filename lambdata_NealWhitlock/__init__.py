"""
lambdata - a collection of data science helper functions
"""

import pandas as pd # These can be imported here because they
import numpy as np  # are in the Pipfile as installs

# sample code for package
ONES = pd.DataFrame(np.ones(10)) # Global variables in all caps
ZEROS = pd.DataFrame(np.zeros(50))
