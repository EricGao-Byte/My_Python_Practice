from scipy.stats import mannwhitneyu

a = [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5]
b = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5]

# 秩和检验
print(mannwhitneyu(a, b, use_continuity=False, alternative='greater'))
