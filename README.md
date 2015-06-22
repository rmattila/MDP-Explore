# MDP-Explore
This is a tool for graphically illustrating the (possibly time-dependent)
Markov chain underlying a *Markov Decision Process* (MDP).

## Usage

First define the transition probabilities of the MDP in `mdp.py` along with the
number of actions and the state labels. A variant of the standard machine
replacement problem is provided as an example in the file.

To run MDP-Explore, type `pythow main.py`. 

The states will be plotted along with the transitions. If *Show probabilities*
is enabled, then the transition probabilities will be added as labels to the
transitions. The thicknesses of the arrows is proportional to the transition
probabilities. You can choose which action and time that should be used to
evaluate the transition matrix.

## Screenshot
![MDP-Explore Screenshot](https://rmattila.github.io/mdp-explore/mdp-explore.png)

## Dependencies
MDP-Explore requires `graphviz` and `wxPython` to run.

