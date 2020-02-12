"""
lambdata - a collection of data science helper functions
"""

import pandas as pd # These can be imported here because they
import numpy as np  # are in the Pipfile as installs

# sample code for package
ONES = pd.DataFrame(np.ones(10)) # Global variables in all caps
ZEROS = pd.DataFrame(np.zeros(50))

def na_filler(dataframe, n=3):
    '''
    Fill the na values of a dataframe by taking the mean of n values above and below the missing value.
    Only works on columns input into function
    '''

    for col in dataframe.describe().columns:
        nums = list(zip(np.where(dataframe.isna())[0],np.where(dataframe.isna())[1]))

    for i in range(len(nums)): # Loop through all of the NaN locations
        values = [] # This will store nearby values in the column
        for j in range(-n,n): # Range to grab nearby values in column
            if (nums[i][0]+j) < 0 or (nums[i][0]+j) >= (len(df)): # Making sure we don't go out of bounds
                continue
            else:
                if (pd.isna(dataframe.iloc[nums[i][0]+j][nums[i][1]])): # Skip if the value is NaN
                    continue
                else:
                    values.append(dataframe.iloc[nums[i][0]+j][nums[i][1]]) # Add to to list
        dataframe.iat[nums[i][0],nums[i][1]] = sum(values)/len(values) # Replace the NaN with the mean
        
    return dataframe