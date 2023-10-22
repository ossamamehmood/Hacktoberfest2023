import numpy as np

def find_outliers(data):
    # Calculate the first quartile (Q1) and third quartile (Q3)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    
    # Calculate the interquartile range (IQR)
    iqr = q3 - q1
    
    # Define the lower and upper bounds for identifying outliers
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Find the indices of outlier values
    outliers = np.where((data < lower_bound) | (data > upper_bound))
    
    return outliers
