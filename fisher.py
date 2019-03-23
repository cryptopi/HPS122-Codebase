import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

HEADS = 1
TAILS = 0
RESOLUTION = 500

sns.set()

def likelihood(x, theta):
    return theta * x + (1 - theta) * (1 - x)

def loglikelihood(x, theta):
    return np.log(likelihood(x, theta))

def score(x, theta):
    return (-1 + 2 * x) / ((1 - theta) * (1 - x) + theta * x)

def entropy(theta):
    return -(1 - theta) * np.log(1 - theta) - theta * np.log(theta)

def fisher(theta):
    return 1 / ((theta) * (1 - theta))

def variance(theta):
    return np.var([score(HEADS, theta), score(TAILS, theta)])

def plot_likelihood():
    x = np.linspace(0, 1, RESOLUTION)
    y_heads = [likelihood(HEADS, theta) for theta in x]
    y_tails = [likelihood(TAILS, theta) for theta in x]
    plt.plot(x, y_heads, label='Heads')
    plt.plot(x, y_tails, label='Tails')
    plt.title('Likelihoods of Heads and tails')
    plt.xlabel('$\\theta$')
    plt.ylabel('Likelihood')
    plt.legend(loc='best')
    plt.savefig('fisher_likelihood.png')
    plt.clf()

def plot_loglikelihood():
    x = np.linspace(0, 1, RESOLUTION)
    y_heads = [loglikelihood(HEADS, theta) for theta in x]
    y_tails = [loglikelihood(TAILS, theta) for theta in x]
    plt.plot(x, y_heads, label='Heads')
    plt.plot(x, y_tails, label='Tails')
    plt.title('Log-Likelihoods of Heads and tails')
    plt.xlabel('$\\theta$')
    plt.ylabel('Log-Likelihood')
    plt.legend(loc='best')
    plt.savefig('fisher_log_likelihood.png')
    plt.clf()

def plot_scores():
    x = np.linspace(0, 1, RESOLUTION)
    y_heads = [score(HEADS, theta) for theta in x]
    y_tails = [score(TAILS, theta) for theta in x]
    plt.plot(x, y_heads, label='Heads')
    plt.plot(x, y_tails, label='Tails')
    axes = plt.gca()
    axes.set_ylim([-15, 15])
    plt.title('Scores of Heads and tails')
    plt.xlabel('$\\theta$')
    plt.ylabel('Score')
    plt.legend(loc='best')
    plt.savefig('fisher_score.png')
    plt.clf()



if __name__ == '__main__':
    # plot_likelihood()
    # plot_loglikelihood()
    # plot_scores()

    # x = np.linspace(0, 1, RESOLUTION)
    # y_var = [variance(theta) for theta in x]
    # y_fisher = [fisher(theta) for theta in x]
    # y_ent = np.array([entropy(theta) for theta in x])
    # plt.plot(x, y_var, label='Var')
    # plt.plot(x, y_fisher, label='Fisher')
    # # plt.plot(x, 3 / y_ent, label='Entropy')
    # plt.plot(x, 3 / y_ent, label='Entropy')
    # axes = plt.gca()
    # axes.set_ylim([0, 15])
    # # plt.title('Scores of Heads and tails')
    # # plt.xlabel('$\\theta$')
    # # plt.ylabel('Score')
    # plt.legend(loc='best')
    # plt.savefig('temp.png')



    N = 5
    x = np.linspace(0, 1, RESOLUTION)
    y_var = [variance(theta) for theta in x]
    y_fisher = np.array([fisher(theta) for theta in x])
    y_fisher = 1 / 2 * np.log(2 * 3.1415927 * (1 / (N * y_fisher) ** 2))
    print(y_fisher)
    y_ent = np.array([entropy(theta) for theta in x])
    plt.plot(x, y_fisher, label='Fisher')
    # plt.plot(x, 3 / y_ent, label='Entropy')
    plt.plot(x, y_ent, label='Entropy')
    axes = plt.gca()
    axes.set_ylim([-5, 2])
    # plt.title('Scores of Heads and tails')
    # plt.xlabel('$\\theta$')
    # plt.ylabel('Score')
    plt.legend(loc='best')
    plt.savefig('temp.png')
