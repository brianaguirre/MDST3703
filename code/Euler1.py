__author__ = 'BrianAguirre'

from Points import points
from math import sqrt

def multiples ():
    count = 0
    for i in range (1, 1001):
        if (i % 3 == 0):
            count += i
            count  = count + i


def distance(one, two):
    pointOne = one
    pointTwo = two
    return sqrt((pointOne.get_x_val()-pointTwo.get_x_val())**2 + ((pointOne.get_y_val()-pointTwo.get_y_val())**2))


point1 = points(1, 2)
point2 = points(1, 4)
print (str(distance(point1, point2)))

