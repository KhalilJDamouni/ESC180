# ESC180 Lab 1
# Connected Cows
# DO NOT modify any function or argument names

import math

def find_euclidean_distance(x1, y1, x2, y2):
    """
    (int, int, int, int) --> float

    Calculates the Euclidean distance between two given 2D points.

    >>> find_euclidean_distance(3.0, 3.0, 2.0, 5.0)
    2.24
    >>> find_euclidean_distance(5.0, 2.0, 4.0, 2.0)
    1.0
    """
    #function body
    return (round(math.sqrt(pow(x1-x2,2) + pow(y1-y2,2)), 2))


def is_cow_within_bounds(cow_position, boundary_points):
    """
    (list, list) --> Boolean

    Given a cow’s position and the boundary points of the cow’s enclosure, determines whether the cow is within the bounds or not.

    >>> is_cow_within_bounds([3, 3], [[2, 5], [5, 5], [5, 1], [2, 1]])
    1
    >>> is_cow_within_bounds([3, 3], [[4, 4], [5, 4], [5, 2], [4, 2]])
    0
    """
    #function body
    if( cow_position[0] > boundary_points[3][0] and \
        cow_position[0] < boundary_points[1][0] and \
        cow_position[1] > boundary_points[3][1] and \
        cow_position[1] < boundary_points[1][1]):
        return 1
    else:
        return 0


def find_cow_distance_to_boundary(cow_position, boundary_point):
    """
    (list, list) --> float

    Given a cow’s position and a boundary point on the cow’s enclosure, returns the shortest distance between the cow and the boundary point.   
    
    >>> find_cow_distance_to_boundary([3, 3], [2, 5])
    2.24
    >>> find_cow_distance_to_boundary([2, 2], [0, 1])
    2.24
    """
    #function body
    return find_euclidean_distance(cow_position[0], cow_position[1], boundary_point[0], boundary_point[1])
    #if I'm not allowed to call another function then here is the body without calling another function:
    #return (round(math.sqrt(pow(cow_position[0]-boundary_point[0],2) + pow(cow_position[1]-boundary_point[1],2)), 2))


def find_time_to_escape(cow_speed, cow_distance):
    """
    (float) --> float

    Given a cow’s speed and its distance from the boundary, returns the time it will take for the cow to reach the boundary. 

    >>> find_time_to_escape(2.0, 8.0)
    4.0
    >>> find_time_to_escape(9.0, 111.0)
    12.33
    """
    #function body
    return (round(cow_distance / cow_speed,2))


def report_cow_status(cow_position1, cow_position2, delta_t, boundary_points):
    """

    (list, list, float, list) --> float OR int


    Given the cow's first position, second position, and the time it took it to travel the distance, 
    as well as the boundary points, provides a report the follows the following rules:
    1. If the cow is within bounds at both time points, it returns the time it would 
       take the cow to escape from its most recent position, at a constance velocity.
    2. If the cow is out of bounds at both time points, it returns the time it would 
       take the cow to travel the distance to boundary_points[0] from its most recent 
       position, at a costant velocity.
    3. If the cow returned to being within the bounds from being out of bounds, returns -1.
    4. If the cow escaped the bounds, return 0.

    >>> report_cow_status([3, 3], [4, 4], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    7.09
    >>> report_cow_status([0, 0], [3, 7], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    2.94
    >>> report_cow_status([0, 0], [3, 3], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    -1
    >>> report_cow_status([3, 3], [3, 6], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    0

    """
    #function body
    velocity = find_euclidean_distance(cow_position1[0], cow_position1[1], cow_position2[0], cow_position2[1]) / delta_t
    if(is_cow_within_bounds(cow_position1,boundary_points) and \
       is_cow_within_bounds(cow_position2,boundary_points)):
        distances = [abs(cow_position2[0] - boundary_points[0][0]), \
                     abs(cow_position2[0] - boundary_points[1][0]), \
                     abs(cow_position2[1] - boundary_points[2][1]), \
                     abs(cow_position2[1] - boundary_points[1][1])]
        return round(min(distances) / velocity, 2)

    if(not is_cow_within_bounds(cow_position1,boundary_points) and \
       not is_cow_within_bounds(cow_position2,boundary_points)):
        return round(find_euclidean_distance(cow_position2[0], cow_position2[1], boundary_points[0][0], boundary_points[0][1]) / velocity,2)

    if(not is_cow_within_bounds(cow_position1,boundary_points) and \
           is_cow_within_bounds(cow_position2,boundary_points)):
        return -1

    if(is_cow_within_bounds(cow_position1,boundary_points) and \
   not is_cow_within_bounds(cow_position2,boundary_points)):
        return 0


if __name__ == '__main__':
    # Test your code by running your functions here, and printing the
    # results to the terminal.
    # This code will not be marked
    print('Testing functions...')
    test = find_euclidean_distance(3.0, 3.0, 2.0, 5.0)
    print(test)
    test = find_euclidean_distance(5.0, 2.0, 4.0, 2.0)
    print(test)
    test = is_cow_within_bounds([3, 3], [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(test)
    test = is_cow_within_bounds([3, 3], [[4, 4], [5, 4], [5, 2], [4, 2]])
    print(test)
    test = find_cow_distance_to_boundary([3, 3], [2, 5])
    print(test)
    test = find_cow_distance_to_boundary([2, 2], [0, 1])
    print(test)
    test = find_time_to_escape(2.0, 8.0)
    print(test)
    test = find_time_to_escape(9.0, 111.0)
    print(test)    
    test = report_cow_status([3, 3], [4, 4], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(test)
    test = report_cow_status([0, 0], [3, 7], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(test)
    test = report_cow_status([0, 0], [3, 3], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(test)
    test = report_cow_status([3, 3], [3, 6], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(test)
