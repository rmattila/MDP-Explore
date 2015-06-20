from numpy import random

def number_of_states():
    return 3

def number_of_controls():
    return 2

def state_labels():
    return {0:'Broken', 1:'Functional'}

def TProb(i, j, k, u):

    return 0.5 * random.rand()
