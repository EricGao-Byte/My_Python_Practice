import numpy as np
import pandas as pd
import scipy.stats as stats
def sign_test(list_c,q,u):
    lst=list_c.copy()
    n=len(lst)
    for i in lst:
        if i<u:
            neg+=1
        elif i>u:
            pos+=1
        else:
            continue
    k=min(neg,pos)
    n1=pos+neg
    p=2*stats.binom.cdf(k,n1,q)
    print('neg:%i  pos:%i  p-value:%f'%(neg,pos,p))
sign_test([95,89,68,90,88,60,81,67,60,60,60,63,60,92,
           60,88,88,87,60,73,60,97,91,60,83,87,81,90],0.75,80)
