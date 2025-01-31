import numpy as np
import pandas as pd
from scipy.stats import ttest_ind, t

# Load the data
data = pd.read_csv('data/A_B_Test_Data.csv')

# Display the first few rows of the data
print(data.head())

# Perform hypothesis testing
old_design = data[data['Design'] == 'Old']['Engagement']
new_design = data[data['Design'] == 'New']['Engagement']

def from_scratch_ttest_ind(sample1, sample2):
    #####################################
    # Implement the t-test from scratch #
    # #### TODO ####                    #
    #####################################
    # 1. Calculate the means of the two samples
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)

    # 2. Calculate the standard deviations of the two samples
    std1 = np.std(sample1, ddof=1)  # ddof=1 for sample standard deviation
    std2 = np.std(sample2, ddof=1)

    # 3. Calculate the standard errors of the two samples
    n1 = len(sample1)
    n2 = len(sample2)
    se1 = std1 / np.sqrt(n1)
    se2 = std2 / np.sqrt(n2)

    # 4. Calculate the t-statistic
    t_stat = (mean1 - mean2) / np.sqrt(se1**2 + se2**2)

    # 5. Calculate the degrees of freedom
    df = n1 + n2 - 2

    # 6. Calculate the p-value using Student's t-distribution
    p_value = 2 * (1 - t.cdf(abs(t_stat), df))
    return t_stat, p_value

t_stat, p_value = from_scratch_ttest_ind(old_design, new_design)
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")
print("From Scratch:")
if p_value < 0.05:
    print("The new design leads to significantly higher user engagement.")
else:
    print("There is no significant difference in user engagement between the old and new designs.")

# We can use the built-in t-test function for comparison
t_stat, p_value = ttest_ind(old_design, new_design)
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")
print("Using ttest_ind:")
if p_value < 0.05:
    print("The new design leads to significantly higher user engagement.")
else:
    print("There is no significant difference in user engagement between the old and new designs.")