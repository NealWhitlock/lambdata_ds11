import pandas as pd

class na_filler(df, n=3):
    '''
    Fill the na values of a dataframe by taking the mean of n values above and below the missing value.
    Only works on numeric columns and is meant for rows where order matters but some values are missing.
    This is will fill values with the mean of proximal values rather than the mean of the entire 
    column in the dataframe.
    '''
    def __init__(self, df):
        self.df = df

    
    for col in df.describe().columns: # Look at only numeric columns
        nums = list(zip(np.where(df.isna())[0],np.where(df.isna())[1])) # Combine indices into list

    for i in range(len(nums)): # Loop through all of the NaN locations
        values = [] # This will store nearby values in the column
        for j in range(-n,n): # Range to grab nearby values in column
            if (nums[i][0]+j) >= 0 and (nums[i][0]+j) < (len(df)): # Make sure we stay in bounds
                if not (pd.isna(df.iloc[nums[i][0]+j][nums[i][1]])): # Skip if the value is NaN
                    values.append(df.iloc[nums[i][0]+j][nums[i][1]]) # Add to to list
        df.iat[nums[i][0],nums[i][1]] = sum(values)/len(values) # Replace the NaN with the mean
        
    return df