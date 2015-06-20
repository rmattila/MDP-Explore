# Define an MDP here

# The following example is a variant of the standard machine replacement
# problem, where as the equipment gets older, the availability of knowledgeable
# service personnel decays and hence the risk of a bad repair increases.

from numpy import exp
from scipy.stats import beta

def number_of_states():
    return 4

def number_of_controls():
    # 0 - Do nothing
    # 1 - Repair
    return 2

def state_labels():
    labels = {}

    labels[0] = 'New'
    labels[1] = 'Used'
    labels[2] = 'Bad'
    labels[3] = 'Broken'

    return labels

def TProb(i, j, k, u):
    if u == 0:
        # Control: Do nothing
        T = [[0.7, 0.2, 0.05, 0.05],
             [0.0, 0.6, 0.2, 0.2],
             [0.0, 0.0, 0.5, 0.5],
             [0.0, 0.0, 0.0, 1.0]]

        return T[i][j]

    else:
        # Control: Repair
        # Probability of successful repair decreases with age

        a = 1.0 + 9.0 * exp(-k / 30.0)
        b  = 1.0 + 500 * exp(-k / 10.0)

        probs = [beta.pdf(((x / 0.95) + 0.25) / 3.0, a, b) for x in range(0, 4)]
        nprobs = [x/sum(probs) for x in probs]

        if nprobs[j] < 10e-4:
            return 0.0

        return nprobs[j]

