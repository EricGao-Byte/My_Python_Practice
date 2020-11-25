import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(
    [25, 45, 50, 54, 55, 61, 64, 68, 72, 75, 75, 78, 79, 81, 83, 84, 84, 84, 85, 86, 86, 86, 87, 89, 89, 89, 90, 91, 91,
     92, 100])
df = pd.DataFrame(s)
df.columns = ['value']
# 做出箱线图
f = plt.boxplot(df['value'], vert=False, patch_artist=False, meanline=True, showmeans=True)
plt.show()
# vert 是否垂直显示箱线图, false为水平
# patch_artist false为Line2D显示
# meanline If True (and showmeans is True), will try to render the mean as a line spanning the full width of the box(以虚线形式表示平均值位置)