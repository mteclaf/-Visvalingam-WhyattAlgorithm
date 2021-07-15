import random
import math
from matplotlib import pyplot as plt
import numpy as np 


MAX_LINE_LENGTH = 10
MIN_LINE_LENGTH = 2

MAX_COORD_LINE = 100
MIN_COORD_LINE = 5

class Point:
    def __init__(self, x, y, id=0):
        self.x = x
        self.y = y
        self.area = 1000000;
        self.not_change = False
        self.id = id

    @staticmethod
    def list_xy_to_points(x: list, y: list) -> list:
        id = 0
        new_list = list()
        for zx, zy in zip(x, y):
            new_list.append(Point(zx ,zy, id))
            id+=1

        return new_list
        #return [Point(px, py) for px, py in zip(x, y)]

    @staticmethod
    def list_points_to_lists(points: list) -> tuple:
        return [(p.x, p.y) for p in points]


def rand_sign(number):
    p_pr_n = random.randint(1, 50)
    if p_pr_n%2 == 0:
        number *= (-1)

    return number

def area(a: Point, b: Point, c: Point):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def intersect_1(a, b, c, d) -> bool:
    if a > b: a, b = b, a
    if c > d: c, d = d, c
    return max(a, c) <= min(b, d)

def are_crossing(line1: tuple, line2: tuple) -> bool:
    a = Point(line1[0], line1[1])
    b = Point(line1[2], line1[3])
    c = Point(line2[0], line2[1])
    d = Point(line2[2], line2[3])

    return (
        intersect_1(a.x, b.x, c.x, d.x) and intersect_1(a.y, b.y, c.y, d.y) and
        ((area(a,b,c) * area(a,b,d)) <= 0) and ((area(c,d,a) * area(c,d,b)) <= 0)
    )

    

def generate_multi_lines(n: int):    

    i = 0
    x_array = [random.randint(MIN_COORD_LINE, MAX_COORD_LINE)]
    y_array = [random.randint(MIN_COORD_LINE, MAX_COORD_LINE)]

    while i < n:
        #calculate coordinates given length
        add_x = random.randint(MIN_LINE_LENGTH, MAX_LINE_LENGTH)
        add_y = random.randint(MIN_LINE_LENGTH, MAX_LINE_LENGTH)


        #random positive or negative number is
        add_x = rand_sign(add_x)
        add_y = rand_sign(add_y)

        new_x = x_array[i] + add_x
        new_y = y_array[i] + add_y

        if i > 1:
            crossed = False
            line_i = 1
            while line_i <= i:
                line1 = (new_x, new_y, x_array[i] - 1, y_array[i] - 1)
                line2 = (x_array[line_i - 1], y_array[line_i - 1], x_array[line_i], y_array[line_i])
                
                if are_crossing(line1, line2):
                    crossed = True
                    break
                line_i += 1

            if not crossed:
                x_array.append(new_x)
                y_array.append(new_y)
                i += 1
            else:
                continue
        
        else:
            x_array.append(new_x)
            y_array.append(new_y)
            i += 1

    return x_array, y_array


def draw_polygon(n: int):

    x = np.random.randint(0,80,n)
    y = np.random.randint(0,80,n)

    #obliczanie punktu środkowego
    center_point = [np.sum(x)/n, np.sum(y)/n]

    #obliczanie kątu
    angles = np.arctan2(x-center_point[0],y-center_point[1])

    #sortowanie w celu kolejnego ich połączenia
    sort_tups = sorted([(i,j,k) for i,j,k in zip(x,y,angles)], key = lambda t: t[2])

    #usuniecie duplikatów
    if len(sort_tups) != len(set(sort_tups)):
         sort_tups = removeDuplicates(sort_tups)

    x,y,angles = zip(*sort_tups)
    x = list(x)
    y = list(y)

    x.append(x[0])
    y.append(y[0])
    
    return x, y


def removeDuplicates(tupl):
    y = []
    for x in tupl:
        if not x in y:
            y += [x]

    return y





if __name__ == "__main__":
    for i in range(5):
        x, y = generate_multi_lines(30)
        fig,ax = plt.subplots()
        ax.plot(x, y)
    plt.show()