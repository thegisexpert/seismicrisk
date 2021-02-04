#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html

from scipy.stats import poisson
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
#Calculate a few first moments:


mu = 0.6
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
#Display the probability mass function (pmf):


x = np.arange(poisson.ppf(0.01, mu),
poisson.ppf(0.99, mu))
#ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
#ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)

ax.plot(x, poisson.cdf(x, mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x, 0, poisson.cdf(x, mu), colors='b', lw=5, alpha=0.5)


#Alternatively, the distribution object can be called (as a function) to fix the shape and location. This returns a frozen RV object holding the given parameters fixed.

#Freeze the distribution and display the frozen pmf:
rv = poisson(mu)
#ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,

#scipy.stats.norm.cdf(2.7, 3, 1) was changed for rv.cdf(x)



ax.vlines(x, 0, norm.cdf(2.7, 3, 1), colors='k', linestyles='-', lw=1,

label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()