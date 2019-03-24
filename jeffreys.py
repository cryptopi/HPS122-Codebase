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

def cot(rad):
    return np.cos(rad) / np.sin(rad)

def csc(rad):
    return 1 / np.sin(rad)

def fisher_theta(theta):
    return 1 / (theta * (1 - theta))

def p_phi(phi):
    if np.pi / 4 < phi and phi < 3 * np.pi / 4:
        return 1 / 2 + (1 / np.pi) * np.arcsin(cot(phi) ** 2)
    else:
        return 1

def p_phi_prime(phi):
    if (np.pi / 4 + EPSILON) < phi and phi < (3 * np.pi / 4 - EPSILON):
        return (2 * cot(phi) * csc(phi) ** 2) / (np.pi * np.sqrt(1 - cot(phi) ** 4))
    else:
        return 0

def fisher_phi(phi):
    if p_phi(phi) == 0 or p_phi(phi) == 1:
        return 0
    heads = (p_phi_prime(phi) / p_phi(phi)) ** 2 * p_phi(phi)
    tails = ((-p_phi_prime(phi) / (1 - p_phi(phi))) ** 2) * (1 - p_phi(phi))
    return heads + tails

def jeffreys(value, fisher, constant=1):
    return np.sqrt(fisher(value)) / constant


def plot_jeffreys():
    x = np.linspace(0, np.pi, int(RESOLUTION * np.pi))
    y = [jeffreys(num, fisher_phi) for num in x]
    probs = [p_phi(num) for num in x]
    plt.plot(probs, y, label='$\\phi$ prior')
    x = np.linspace(0, 1, RESOLUTION)
    y = [jeffreys(num, fisher_theta, constant=1) for num in x]
    probs = x
    plt.plot(probs, y, label='$\\theta$ prior')
    plt.title('Jeffreys Priors')
    plt.xlabel('Probability of Heads')
    plt.ylabel('PDF')
    plt.legend(loc='best')
    plt.savefig('images/jeffreys.png')
    plt.clf()

plot_jeffreys()
