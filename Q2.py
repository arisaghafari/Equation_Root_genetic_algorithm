import random
import numpy as np

class GLA(object):
    def __init__(self, pop_size):
        self.pop_size = pop_size

    def fitness(self):
        pass

    def selection(self):  # using generation gap approach
        pass

    def cross_over(self):
        pass

    def mutation(self, old_populations, num):
        pass


def equation(x):
    return 9 * x ** 5 - 194.7 * x ** 4 + 1680.1 * x ** 3 - 7227.94 * x ** 2 + 15501.2 * x - 13257.2

if __name__ == "__main__":
    pop_size = 40
    gla = GLA(pop_size)