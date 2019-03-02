import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.integrate import quad as integrate

def make_p(e):
    return lambda x : (e + 1) * x ** e

def entropy(p):
    answer, err = integrate(lambda x : p(x) * np.log(p(x)), 0, 1)
    return -answer

x = range(109)
y = [entropy(make_p(e)) for e in x]
plt.plot(x, y)
# plt.ylim(top=0.5)
plt.xlabel('Exponent')
plt.ylabel('Continuous Shannon Entropy')
plt.title('Continuous Entropy Monomial Divergence')
plt.savefig('decaying_continuous.png')
