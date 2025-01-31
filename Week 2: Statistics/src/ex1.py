import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Week 2: Statistics/data/Student_Scores_Data.csv')

# Display the first few rows of the data
print(data.head())

# Compute descriptive statistics

###################################
# Compute the statistics here     #
mean = np.mean(data['Score'])
median = np.median(data['Score'])
std_dev = np.std(data['Score'])

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
###################################

# Check out numpy's functions for calculating these statistics
# Here: https://numpy.org/doc/stable/reference/routines.statistics.html#averages-and-variances

# Visualize the data using histograms, box plots, scatter plots, and bar charts

###################################
# Visualize the data here         #
# #### TODO ####                  #
###################################

# Check out matplotlib's functions for creating these visualizations
# Here: https://matplotlib.org/stable/gallery/index.html