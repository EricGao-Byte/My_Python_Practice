import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics
x=[[274,2450],[180,3254],[375,3802],[205,2838],[86,2347],[265,3782],[98,3008],[330,2450],[195,2137],[53,2560],[430,4020],[372,4427],[236,2660],[157,2088],[370,2605]]
y=[162,120,223,131,67,169,81,192,116,55,252,232,144,103,212]
linreg=LinearRegression()
linreg.fit(x,y)
print(linreg.intercept_,linreg.coef_)
y_per=linreg.predict(x)
print("y_per",y_per)
err=metrics.mean_squared_error(y,y_per)
print(err)
decision_score=linreg.score(x,y)
print(decision_score)