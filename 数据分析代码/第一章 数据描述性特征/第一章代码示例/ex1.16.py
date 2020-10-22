import scipy
from scipy.stats import pearsonr, spearmanr
import numpy as np

x = np.array([67, 54, 72, 64, 39, 22, 58, 43, 46, 34])
y = np.array([24, 15, 23, 19, 16, 11, 20, 16, 17, 13])
# pearsonr
r_row, p_value = pearsonr(x, y)
print(r_row)
print(p_value)
# spearmanr
rho, p_value = spearmanr(x, y)
print(rho)
print(p_value)
