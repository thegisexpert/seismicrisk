from scipy.stats import lognorm
import matplotlib.pyplot as plt
import numpy as np
import pylab

fig, ax = plt.subplots(1, 1)
s = 0.954
mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')

x = np.linspace(lognorm.ppf(0.01, s),
                lognorm.ppf(0.99, s), 100)
x1 = [0.5, 4, 8]
#x = np.concatenate(x , x1)
ax.plot(x, lognorm.pdf(x, s),
       'r-', lw=5, alpha=0.6, label='lognorm pdf')


rv = lognorm(s)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

s2=0.5
ax.plot(x1, lognorm.pdf(x1, s2),
       'g-', lw=6, alpha=0.7, label='lognorm pdf v2')


y = rv.pdf(x)
print " x " + str(x1)
print " r " + str(rv.pdf(x1))
#ojo se guinda

vals = lognorm.ppf([0.001, 0.5, 0.999], s)
np.allclose([0.001, 0.5, 0.999], lognorm.cdf(vals, s))

r = lognorm.rvs(s, size=1000)




ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)

plt.show()

'''
#https://scipy.github.io/devdocs/generated/scipy.stats.lognorm.html
'''

#https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python