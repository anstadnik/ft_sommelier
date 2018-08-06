## Importing things
import pandas as pd
import matplotlib.pyplot as plt
import random
## Load data
red_wine = pd.read_csv("./resources/resources/winequality-red.csv", sep=';')
## V.1 a)
class perceptron:
    """A simple perceptron, has randomly initialized weights and bias"""
    def __init__(self, amount):
        """Random data initialization"""
        self.weights = [random.random() for n in amount]
        self.bias = random.random()
##

##
