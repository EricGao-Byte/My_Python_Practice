
from scipy.stats import wilcoxon

a = [459,367,303,392,310,342,421,446,430,412]
b = [414,306,321,443,281,301,353,391,405,390]

print(wilcoxon(a,b,zero_method = 'wilcox',correction = 'False',alternative = 'greater'))