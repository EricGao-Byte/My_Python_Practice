import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import statsmodels.api as sm



x=[[1,2.5,0,0],[1,173.0,2,0],[1,119.0,2,0],[1,10.0,2,0],[1,502.2,2,0],[1,4.0,0,0],[1,14.4,0,1],[1,2.0,2,0],[1,40.0,2,0],[1,6.6,0,0],[1,21.4,2,1],[1,2.8,0,0],[1,2.5,0,0],[1,6.0,0,0],[1,3.5,0,1],[1,62.2,0,0],[1,10.8,0,1],[1,21.6,0,1],[1,2.0,0,1],[1,3.4,2,1],[1,5.1,0,1],[1,2.4,0,0],[1,1.7,0,1],[1,1.1,0,1],[1,12.8,0,1],[1,1.2,2,0],[1,3.5,0,0],[1,39.7,0,0],[1,62.4,0,0],[1,2.4,0,0],[1,34.7,0,0],[1,28.4,2,0],[1,0.9,0,1],[1,30.6,2,0],[1,5.8,0,1],[1,6.1,0,1],[1,2.7,2,1],[1,4.7,0,0],[1,128.0,2,1],[1,35.0,0,0],[1,2.0,0,0],[1,8.5,0,1],[1,2.0,2,1],[1,2.0,0,1],[1,4.3,0,1],[1,244.8,2,1],[1,4.0,0,1],[1,5.1,0,1],[1,32.0,0,1],[1,1.4,0,1]]
y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
print(x)  # 查看样本

model=sm.Logit(y,x).fit()
print(model.summary())
