import random
import numpy as np

pop_len = 16

class GA(object):
    def __init__(self, pop_size):
        self.pop_size = pop_size
        self.pop_list = []
        self.result = None
        for _ in range(pop_size):
            temp = ''
            for _ in range(pop_len):
                temp += str(random.randint(0, 1))
            self.pop_list.append([temp, 0])

        for i in range(1000):
            self.fitness_list = self.fitness()
            self.selection()
            if self.result:
                print("result : ", self.result)
                break
            for i in range(int(len(self.pop_list) * 0.7)):
                pos1 = random.randint(0, len(self.pop_list))
                pos2 = random.randint(0, len(self.pop_list))
                a1 = self.pop_list[pos1][0]
                a2 = self.pop_list[pos2][0]
                self.pop_list[pos1][0], self.pop_list[pos2][0] = self.cross_over(self.pop_list[pos1][0], self.pop_list[pos2][0])

            for i in range(int(self.pop_size * 0.3)):
                #pos = random.randrange(0, len(self.pop_list))
                pos = 3
                self.div_mutation(self.pop_list[pos][0])
            print("iteration : ", i)

    def fitness(self):
        fitness_list = []
        for i in range(len(self.pop_list)):
            decimal = bin_to_decimal(self.pop_list[i][0])
            e = equation(decimal)
            fitness_list.append(e)
            self.pop_list[i][1] = e
            if abs(e) <= 0.01 :
                self.result = self.pop_list[i]

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
                del self.pop_list[j - count]
                count += 1

    def cross_over(self, pop1, pop2):
        div1 = 4
        div2 = 12
        temp_pop1 = pop1[:div1] + pop2[div1:div2] + pop1[div2:]
        temp_pop2 = pop2[:div1] + pop1[div1:div2] + pop2[div2:]
        return temp_pop1, temp_pop2

    def div_mutation(self, pop):
        # div1 = random.randrange(0, pop_len)
        # div2 = random.randrange(0, pop_len)
        div1 = 4
        div2 = 12
        if div1 > div2:
            self.mutation(div1, div2, pop)
        elif div2 > div1:
            self.mutation(div2, div1, pop)

    def mutation(self, div1, div2, pop):
        temp = ''
        for i in range(div1 - div2):
            temp += str(random.randint(0, 1))
        temp_pop1 = pop[:div1] + temp + pop[div2:]
        self.pop_list.append([temp_pop1, 0])

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