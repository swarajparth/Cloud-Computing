
'''
Name - SHYAM MARJIT
ROll No - 1901195
Email - shyam.marjit@iiitg.ac.in
'''
from typing import Callable, List
import math

def compute_distance(point_a: List[float], point_b: List[float])->float:
    distance = 0
    for i in range(len(point_a)):
        distance = distance + (point_a[i]-point_b[i])**2
    return math.sqrt(distance)

class DistanceFuncs:
    def calc_distance(self, point_a: List[float], point_b: List[float], dist_func: Callable)->float:
        """ Compute distance between two points using the passed compute_distance function. """
        return compute_distance(point_a, point_b)

    def euclidean(self, point_a: List[float], point_b: List[float],/)->float:
        """ Compute Euclidean Distance between two points. """
        return math.dist(point_a, point_b)

    def manhattan_distance(self, point_a: List[float], point_b: List[float])->float:
        """ Compute the manhattan_distance between two points. """
        distance = 0
        for i in range(len(point_a)):
            distance = distance + abs(point_a[i] - point_b[i])
        return distance

    def jaccard_distance(self, point_a: List[float], point_b: List[float])->float:
        """ Compute the jaccard_distance between two points. """
        return 1 - (len(set(point_a)&set(point_b))/(len(set(point_a)) + len(set(point_b)) - len(set(point_a)&set(point_b))))

def main():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [4, 5, 6, 7, 8]
    distance = DistanceFuncs()
    print('Point one: ', list_1, '\nPoint two: ', list_2)
    print('Normal Distance: ', distance.calc_distance(list_1, list_2, compute_distance))
    print('Eucleaden Distance: ', distance.euclidean(list_1, list_2))
    print('Manhattan Distance: ', distance.manhattan_distance(list_1, list_2))
    print('Jaccardian Distance: ', distance.jaccard_distance(list_1, list_2))

if __name__ =="__main__":
    main()
