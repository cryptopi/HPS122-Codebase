import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

HEADS = 1
TAILS = 0
RESOLUTION = 500

sns.set()

def fisher(theta):
    return np.cos(rad) / np.sin(rad)

def csc(rad):
    return 1 / np.sin(rad)

def make_circle(radius):
    x = np.linspace(0, radius, RESOLUTION * radius)
    y = np.sqrt(radius ** 2 - x ** 2)
    plt.plot(x, y)
    axes = plt.gca()
    axes.set_aspect('equal')

def plot_points(func, samples, name, marker, s=65, low=0, high=1):
    inputs = np.linspace(low, high, samples)
    heads = np.array([func(num) for num in inputs])
    tails = 1 - heads
    heads = 2 * np.sqrt(heads)
    tails = 2 * np.sqrt(tails)
    plt.scatter(heads, tails, marker=marker, label=name, s=s)


def make():
    make_circle(2)
    plot_points(phi, 30, '$\\phi$', 'o', s=115, low=0, high=np.pi)
    plot_points(theta, 30, '$\\theta$', '^', low=0, high=1)
    plt.title('Model Space and Uniformity')
    plt.xlabel('Scaled Probability of Heads')
    plt.ylabel('Scaled Probability of Tails')
    plt.legend(loc='best')
    plt.savefig('images/model_space_uniformity.png')
    plt.clf()

make()
