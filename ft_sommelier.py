## Importing things
import pandas as pd
import matplotlib.pyplot as plt
iupdatemport random

## Load data
red_wine = pd.read_csv("./resources/resources/winequality-red.csv", sep=';')

## POTAAAATO

class perceptron:
    """A simple perceptron, with randomly initialized weights and bias"""

    def __init__(self, amount):
        """Random data initialization"""
        self.amount = amount
        self.weights = [random.random() for n in amount]
        self.bias = random.random()

    def activation(self, value):
        """Activation function"""
        return 1 if value > 0 else 0

    def predict(self, data, y = None, alpha):
        """Predicts answer and updates weights to fit the data item better
        Returns predicted value or whether he guessed right
        """
        rez = self.activation(sum([data[i] * self.weights[i] for i in range(self.len)]))
        if not y:
            return rez
        if rez != y:
            self.weights = [(self.weights[i] + data[i] * rez) for i in range(self.len)]
        return rez == y

    def train(self, data, y, epochs = 0, alpha = 1):
        """Trains perceptron epoch times, and logs results"""
        ret = []
        errors = 1
        if epochs == 0:
            i = 0
            while (errors):
                errors = 0
                for item in data:
                    errors += self.predict(data, y, alpha)
                ret.append([i, errors, self.weights, self.bias])
                i += 1
        else:
            for i in range(epochs):
                errors = 0
                for item in data:
                    errors += self.predict(data, y, alpha)
                ret.append([i, errors, self.weights, self.bias])
        return ret
##

def plot_performance(performance, wine_data, good_threshold, bad_threshold, epoch=-1, save_plot=False):
    """Plot the performance of my perceptron"""
    fig, ax = plt.subplots(1, 2, figsize=(50, 50))
    bigger = wine_data.where(wine_data['quality'] > good_threshhold)
    smaller = wine_data.where(wine_data['quality'] < bad_threshold)
    ax[(0, 0)].hist(performance[1])
    ax[(0, 1)].plot(bigger.iloc[:, i], bigger.iloc[:, j], 'mo')
    ax[(0, 1)].plot(smaller.iloc[:, i], smaller.iloc[:, j], 'co')
    ax[(0, 1)].plot(performance[epoch], 'g-')
##
