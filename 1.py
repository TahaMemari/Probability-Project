#import necessary libraries
import numpy as np
from markovchain import MarkovChain

#initialize the transition matrix as a 2D array
P = np.array([[0.5, 0, 0, 0, 0.5],
              [0, 0.5, 0, 0.5, 0],
              [0, 0, 1, 0, 0],
              [0, 0.25, 0.25, 0.25, 0.25],
              [0.5, 0, 0, 0, 0.5]])
#Draw graph of the transition matrix
tg = MarkovChain(P, ['1', '2', '3', '4', '5'])
tg.draw("Q1.png")