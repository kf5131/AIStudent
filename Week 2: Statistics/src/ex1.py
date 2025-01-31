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

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Histogram
axes[0, 0].hist(data['Score'], bins=10, edgecolor='black')
axes[0, 0].set_xlabel('Score')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Histogram of Student Scores')

# Box plot
axes[0, 1].boxplot(data['Score'], vert=False)
axes[0, 1].set_ylabel('Score')
axes[0, 1].set_title('Box Plot of Student Scores')

# Scatter plot
axes[1, 0].scatter(data['Score'], data['Student_ID'])
axes[1, 0].set_xlabel('Score')
axes[1, 0].set_ylabel('Student_ID')
axes[1, 0].set_title('Scatter Plot of Student Scores vs Student_ID')

# Bar chart
axes[1, 1].bar(data['Student_ID'], data['Score'])
axes[1, 1].set_xlabel('Student_ID')
axes[1, 1].set_ylabel('Score')
axes[1, 1].set_title('Bar Chart of Student Scores')
# Rotate x-axis labels for better readability
axes[1, 1].tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()

##################################

# Check out matplotlib's functions for creating these visualizations
# Here: https://matplotlib.org/stable/gallery/index.html