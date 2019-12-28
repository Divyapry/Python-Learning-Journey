import sys
sys.path.append("NumPy_path")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

trials = 1000
n = 10
p = 0.5

def run_binom(trials,n,p):
    heads=[]
    for i in range(trials):
        tosses=[np.random.random() for i in range(n)]
        heads.append(len([i for i in tosses if i>=0.50]))
        print('HEADS IS:',heads)
    return heads

heads= run_binom(trials,n,p)

fig,ax = plt.subplots(figsize=(14,7))
ax = sns.distplot(heads, bins=11, label='simulation results')

ax.set_xlabel("number of heads",fontsize=16)
ax.set_ylabel("frequency",fontsize=16)

from scipy.stats import binom
x = range(0,11)
ax.plot(x, binom.pmf(x, n, p), 'ro', label='actual binomial distribution')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='r', lw=5, alpha=0.5)
plt.legend()
plt.show()

print(np.random.binomial(n,p))



runs = 10000
prob_6 = sum(1 for i in np.random.binomial(n,p,size=runs) if i==6)/runs
print('the probability of 6 heads is: '+str(prob_6))
print(sum(1 for i in np.random.binomial(n,p,size=runs) if i==6))
