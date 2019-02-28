import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import beta

THETA = 0.5
TRIAL_COUNT = 20

class BetaDistribution:

    def __init__(self, a, b):
        self.a = a
        self.b = b

def compute_c1(a, b):
    return math.factorial((a + b - 1)) / (math.factorial((a - 1)) * math.factorial((b - 1)))

def compute_c2(outcome, N):
    return math.factorial(N) / (math.factorial(outcome) * math.factorial(N - outcome))

def compute_c3(a, b, outcome, N):
    return math.factorial(a + b + N - 1) / (math.factorial(a + outcome - 1) * math.factorial(b + N - outcome - 1))

def update_distribution(prior, outcome):
    if outcome: # heads
        return BetaDistribution(prior.a + 1, prior.b)
    else:
        return BetaDistribution(prior.a, prior.b + 1)

def get_coin_flip():
    return np.random.uniform(0, 1) < THETA


x = np.arange (0, 1000) / 1000
values = [((0, 0, 1), BetaDistribution(15, 5)), ((1, 0, 0), BetaDistribution(1, 1))]
for color_components, prior in values:
    for trial_number in range(TRIAL_COUNT):
        y = beta.pdf(x, prior.a, prior.b)
        opacity = trial_number / TRIAL_COUNT * 0.9 + 0.1
        color = (*color_components, opacity)
        plt.plot(x, y, color=color)
        outcome = get_coin_flip()
        prior = update_distribution(prior, outcome)
    print(f'Largest y at: {np.argmax(y) / 1000}')
plt.xlabel('Theta')
plt.ylabel('Probability')
plt.title('Beta Prior Convergence')
plt.savefig('test.png')
