from scipy.stats import lognorm
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)
s = 0.954  #signa desviacion estandar
mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')

x = np.linspace(lognorm.ppf(0.01, s),
                lognorm.ppf(0.99, s), 100)
x1 = [0.5, 4, 8]
#x = np.concatenate(x , x1)
ax.plot(x, lognorm.pdf(x, s),
       'r-', lw=5, alpha=0.6, label='lognorm pdf 0.9')



s = 0.7  #signa desviacion estandar
mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')

x = np.linspace(lognorm.ppf(0.01, s),
                lognorm.ppf(0.99, s), 100)
x1 = [0.5, 4, 8]
#x = np.concatenate(x , x1)
ax.plot(x, lognorm.pdf(x, s),
       'r-', lw=5, alpha=0.6, label='lognorm pdf 0.7')

s = 0.4  #signa desviacion estandar
mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')

x = np.linspace(lognorm.ppf(0.01, s),
                lognorm.ppf(0.99, s), 100)
x1 = [0.5, 4, 8]
#x = np.concatenate(x , x1)
ax.plot(x, lognorm.pdf(x, s),
       'r-', lw=5, alpha=0.6, label='lognorm pdf 0.4')


rv = lognorm(s)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

y = rv.pdf(x)


print " x " + str(x1)
print " r " + str(rv.pdf(x1))
#ojo se guinda

ax.plot([0.1,0.2,0.3,0.5])

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