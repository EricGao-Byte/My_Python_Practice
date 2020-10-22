import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(
    [25, 45, 50, 54, 55, 61, 64, 68, 72, 75, 75, 78, 79, 81, 83, 84, 84, 84, 85, 86, 86, 86, 87, 89, 89, 89, 90, 91, 91,
     92, 100])
df = pd.DataFrame(s)
df.columns = ['value']
f = plt.boxplot(df['value'], vert=False, patch_artist=False, meanline=True, showmeans=True)
plt.show()
