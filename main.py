
from functools import reduce


numbers = [     [10, 11, 12, 13, 14],
               [20, 21, 22, 23, 24],
               [30, 31, 32, 33, 34]]


for i in range(len(numbers[0])):
       csum = 0
       for j in range(len(numbers)):
               csum += numbers[j][i]
       print ("The summation of column {0}: {1}".format(i, csum))


# sum(list(zip(numbers[0], numbers[1], numbers[2]))[0])
# sum(list(zip(numbers[0], numbers[1], numbers[2]))[1])
# sum(list(zip(numbers[0], numbers[1], numbers[2]))[2])
# sum(list(zip(numbers[0], numbers[1], numbers[2]))[3])
# sum(list(zip(numbers[0], numbers[1], numbers[2]))[4])
