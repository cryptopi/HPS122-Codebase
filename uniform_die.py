import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import beta

x = range(6)
probabilities = [1 / 6 for i in x]

plt.bar(x, probabilities, tick_label=[i + 1 for i in x])
plt.ylim(top=0.5)
plt.xlabel('Face Number')
plt.ylabel('Probability')
plt.title('POI Die Prior')
plt.savefig('uniform_die.png')
