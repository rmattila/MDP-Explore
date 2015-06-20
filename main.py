import graphviz as gv

# Define the MDP in mdp.py
from mdp import *

def generateMDPGraph(u, k, labels):

    line_width = 5.0

    if u > number_of_controls():
        print "ERROR: %i is not a valid control action!" % u
        u = 0

    mdp = gv.Digraph(format='pdf')

    # Create the nodes in the graph
    for i in range(0, number_of_states()):
        if i in labels:
            mdp.node(str(i), str(i) + ':' + labels[i])
        else:
            mdp.node(str(i), 'Node %i' % i)

    # Add edges
    for i in range(0, number_of_states()):
        psum = 0.0
        for j in range(0, number_of_states()):
            p = TProb(i, j, k, u)

            if TProb(i, j, k, u) > 0:
                mdp.edge(str(i), str(j), '%.2f' % p, {'penwidth':str(line_width * p)})
                psum += p

        if psum != 1.0:
            print "WARNING: The transition matrix has a row (%i) that does not sum to one!" % i

    return mdp

def plotMDPGraph(mdp):
    filename = mdp.render(filename='img/mdp')
    print "Graph of MDP was rendered to " + filename


plotMDPGraph(generateMDPGraph(0, 0, state_labels()))
