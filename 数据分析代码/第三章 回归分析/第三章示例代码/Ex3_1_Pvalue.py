import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import statsmodels.api as sm

x=[[1,274,2450],[1,180,3254],[1,375,3802],[1,205,2838],[1,86,2347],[1,265,3782],[1,98,3008],[1,330,2450],[1,195,2137],[1,53,2560],[1,430,4020],[1,372,4427],[1,236,2660],[1,157,2088],[1,370,2605]]
y=[162,120,223,131,67,169,81,192,116,55,252,232,144,103,212]
model=sm.OLS(y,x).fit()
sm.stats.linear_rainbow(model)
model.summary()