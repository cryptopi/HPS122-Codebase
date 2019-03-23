import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

RESOLUTION = 500
EPSILON = .01

sns.set()

def cot(rad):
    return np.cos(rad) / np.sin(rad)

def csc(rad):
    return 1 / np.sin(rad)

def uniform_theta(theta):
    return 1

def uniform_phi(phi):
    return 1

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

def p_theta_prime(theta):
    if 0.5 < theta and theta < 1:
        return (np.pi * np.cos(1/2 * np.pi * (-1 + 2 * theta))) / (2 * np.sqrt(np.sin(1/2 * np.pi * (-1 + 2 * theta))) * (1 + np.sin(1/2 * np.pi * (-1 + 2 * theta))))
    else:
        return None

def plot_uniform_theta():
    x = np.linspace(0, 1, RESOLUTION)
    y = [uniform_theta(phi) for phi in x]
    plt.plot(x, y, label='Plot')
    axes = plt.gca()
    axes.set_ylim([0, 3])
    plt.title('Prior on Uniform $\\theta$')
    plt.xlabel('$\\theta$')
    plt.ylabel('Probability')
    plt.savefig('images/uniform_theta.png')
    plt.clf()

def plot_uniform_phi():
    x = np.linspace(0, 1, RESOLUTION)
    y = [uniform_phi(phi) for phi in x]
    plt.plot(x, y, label='Plot')
    axes = plt.gca()
    axes.set_ylim([0, 3])
    plt.title('Prior on Uniform $\\phi$')
    plt.xlabel('$\\phi$')
    plt.ylabel('Probability')
    plt.savefig('images/uniform_phi.png')
    plt.clf()

def transformed_phi(phi):
    return 1 * np.abs(p_phi_prime(phi))

def plot_transformed_phi():
    x = np.linspace(0, np.pi, int(RESOLUTION * np.pi))
    y = [transformed_phi(phi) for phi in x]
    plt.plot(x, y, label='Plot')
    axes = plt.gca()
    plt.title('Prior on $\\phi$ From Jacobian Transform')
    plt.xlabel('$\\phi$')
    plt.ylabel('Probability')
    plt.savefig('images/transformed_phi.png')
    plt.clf()

def transformed_theta(phi):
    return 1 * np.abs(p_theta_prime(phi))

def plot_transformed_theta():
    x = np.linspace(0.5, 1, int(RESOLUTION * 0.5))
    y = [p_theta_prime(theta) for theta in x]
    plt.plot(x, y, label='Plot')
    axes = plt.gca()
    plt.title('Prior on $\\theta$ From Jacobian Transform')
    plt.xlabel('$\\theta$')
    plt.ylabel('Probability')
    plt.savefig('images/transformed_theta.png')
    plt.clf()


plot_uniform_phi()
plot_uniform_theta()
plot_transformed_phi()
plot_transformed_theta()
