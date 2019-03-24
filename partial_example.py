import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

HEADS = 1
TAILS = 0
RESOLUTION = 500
EPSILON = .01

sns.set()

def plot_dice():
    x = list(range(1, 7))
    y = [0.0544, 0.0788, 0.1142, 0.1654, 0.2398, 0.3475]
    plt.bar(x, y)
    plt.title('Partial Information Solution')
    plt.xlabel('Die Face')
    plt.ylabel('Probability')
    plt.savefig('images/maxent_partial.png')
    plt.clf()

plot_dice()
