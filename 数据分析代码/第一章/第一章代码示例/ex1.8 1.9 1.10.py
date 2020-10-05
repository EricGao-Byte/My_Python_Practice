from itertools import groupby
nums2=[25,45,50,54,55,61,64,68,72,75,75,78,79,81,83,84,84,84,85,86,86,86,87,89,89,89,90,91,91,92,100]
for k, g in groupby(sorted(nums2), key=lambda x: int(x) // 10):
    lst = map(str, [int(y) % 10 for y in list(g)])
    print (k, '|', ' '.join(lst))



import pandas as pd
from stemgraphic import stem_graphic
import matplotlib.pyplot as plt
a=[126,149,143,141,127,123,137,132,135,134,146,142,135,141,150,137,144,137,134,137,148,144,142,137,147,138,140,132,149,131,139,142,138,145,147,137,135,142,151,146,129,120,143,145,142,136,147,128,142,132,138,139,147,128,139,146,139,131,138,149]
stem_graphic(a)
plt.show()

