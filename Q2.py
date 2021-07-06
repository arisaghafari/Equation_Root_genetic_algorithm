import random
import numpy as np

pop_len = 16

class GA(object):
    def __init__(self, pop_size):
        self.pop_size = pop_size
        self.pop_list = []
        for _ in range(pop_size):
            temp = ''
            for _ in range(pop_len):
                temp += str(random.randint(0, 1))
            self.pop_list.append([temp, 0])

        self.fitness_list = self.fitness()
        self.selection()
        a = 2
    def fitness(self):
        fitness_list = []
        for i in range(len(self.pop_list)):
            decimal = bin_to_decimal(self.pop_list[i][0])
            e = equation(decimal)
            fitness_list.append(e)
            self.pop_list[i][1] = e

        return fitness_list

    def selection(self):  # using generation gap approach
        remove_num = int(self.pop_size * 0.3)
        remove_list = []
        self.fitness_list.sort()
        for i in range(remove_num):
            remove_list.append(self.fitness_list[len(self.fitness_list) - 1 - i])
        count = 0
        for j in range(len(self.pop_list)):
            if self.pop_list[j - count][1] in remove_list:
                a = self.pop_list[j - count][1]
                del self.pop_list[j - count]
                count += 1

    def cross_over(self):
        pass

    def mutation(self, old_populations, num):
        pass


def equation(x):
    return 9 * x ** 5 - 194.7 * x ** 4 + 1680.1 * x ** 3 - 7227.94 * x ** 2 + 15501.2 * x - 13257.2

def decimal_to_bin(decimal):
    bin = decimal
    return bin

def bin_to_decimal(bin):
    temp1 = 0
    temp2 = 0
    for i in range(int(pop_len / 2)):
        temp1 += int(bin[i]) * 2 ** (int(pop_len / 2) - 1 - i)
        temp2 += int(bin[i + int(pop_len / 2)]) * 2 ** (-(i + 1))
    temp2 /= 10 ** int(pop_len / 2)
    temp1 += temp2
    return temp1

if __name__ == "__main__":
    pop_size = 10
    ga = GA(pop_size)
    print(ga.pop_list)