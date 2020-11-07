
from scipy.stats import wilcoxon

a = [14,18,2,4,-5,14,-3,-1,1,6,3,3]
b = [8,26,-7,-1,2,9,0,-4,13,3,3,4]

print(wilcoxon(a,b,zero_method='zsplit'))