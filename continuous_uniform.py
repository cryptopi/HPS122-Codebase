import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.integrate import quad as integrate

def make_discrete_uniform(bin_count):
    return lambda x : 1 / bin_count

def make_continuous_uniform(height):
    return lambda x : height

def continuous_entropy(p, start, end):
    answer, err = integrate(lambda x : p(x) * np.log(p(x)), start, end)
    return -answer

def discrete_entropy(p, items):
    sum = 0
    for item in items:
        sum += p(item) * np.log(p(item))
    return -sum

bin_counts = range(1, 1000)
uniform_target = make_continuous_uniform(0.1)
discrete_y = [discrete_entropy(make_discrete_uniform(bin_count), range(1, bin_count)) for bin_count in bin_counts]
plt.plot(bin_counts, discrete_y, label='Discrete Uniform Entropy')
c_entropy = continuous_entropy(uniform_target, 0, 10)
plt.plot(bin_counts, [c_entropy] * len(bin_counts), label='Continuous entropy of $p(x) = 0.5$')
plt.xlabel('|S|')
plt.ylabel('Entropy')
plt.title('Violation of Strict Increase in $|S|$')
plt.legend(loc = 'best')
plt.savefig('continuous_vs_discrete_uniform.png')
plt.clf()


heights = np.array(range(1, 500)) / 1000
continuous_entropies = [continuous_entropy(make_continuous_uniform(height), 0, 1 / height) for height in heights]
plt.plot(heights, continuous_entropies)
plt.title('Entropies of Continuous Constant PDFs')
plt.xlabel('$p(x)$ uniform height')
plt.ylabel('Continuous Entropy')
plt.savefig('continuous_uniform.png')
