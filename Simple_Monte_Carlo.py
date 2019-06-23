import random
import matplotlib.pyplot as plt
import pandas as pd

S0 = 24
r = 0.12
sigma = 0.08
t = 1/365

def GeoBrownianMotion(S0):
    price_list = []
    while True:
        delta_S = r*t + 0.15*(t**0.5)*random.normalvariate(0,1)
        S0 = S0 + delta_S
        price_list.append(S0)
        
        if len(price_list) >= 1000:
            break
    return price_list

for i in range(0,8):
    price_list = GeoBrownianMotion(S0)
    price_df = pd.Series(price_list)
    price_df.plot()
    #plt.close('all') 

plt.show()
