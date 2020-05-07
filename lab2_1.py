import math

def vector_from_points(p1, p2):
    ''' 
    (List[int], List[int]) -> List[int]

    Returns a list of n components, representing a vector that has its tail at 
    p1 and its head at p2. (If n is zero, returns an empty list.)

    >>> vector_from_points([0, 0], [1, 2])  
    [1, 2]
    >>> vector_from_points([3, -1, 0], [10, 0, 1])
    [7, 1, 1]
    '''

    result = []
    for x in range(0, len(p1)):
        result.append(p2[x] - p1[x])
    return result

def vector_length(v):
    ''' 
    (List[int]) -> float

    Returns a floating-point value indicating the magnitude of an n-element vector, v. 
    If the input vector is an empty list, returns -1.

    >>> vector_length([2, 1]) 
    2.23606797749979
    >>> vector_length([]) 
    -1
    '''

    if(not len(v)):
        return -1
    length = 0
    for x in v:
        length += pow(x, 2)
    return math.sqrt(length)


def angle_between(v, w):
    ''' 
    (List[int], List[int]) -> float

    Returns the angle, in degrees, between two vectors v and w.

    >>> angle_between([-1], [2])  
    180.0
    >>> angle_between([0, 1, 0, 1], [1, 3, 4, 5])
    37.61611202673532
    '''

    return (math.acos(dot_product(v,w) / ((vector_length(v)) * vector_length(w))) / math.pi) * 180

def dot_product(v,w):
    ''' 
    (List[int], List[int]) -> int

    Returns the dot product of two vectors v and w.

    >>> dot_product( [-1], [2])   
    -2
    >>> dot_product( [0, 1, 0, 1], [1, 3, 4, 5])    
    8

    '''
    length = 0
    for x in range(0, len(v)):
        length += v[x]*w[x]
    return length

def unit_vector(v):
    ''' 
    (List[int]) -> List[float]

    Returns an n-element list that represents a unit vector in the same direction as v.
    Returns an empty list if n equals 0.

    >>> unit_vector([2, 1])
    [0.8944271909999159, 0.4472135954999579]
    >>> unit_vector([])
    []
    '''
    result = []
    length = vector_length(v)
    for x in range(0, len(v)):
        result.append(v[x] / length)
    return result

def cross_product(v,w):
    ''' 
    (List[int], List[int]) -> List[int]

    If the size of v or w is:
    1. Bigger than 3:
        Returns an empty list.
    2. Smaller than 3:
        Returns the cross product of v and w assuming that the missing elements are 0.
    3. Equal to 3:
        Returns the cross product of v and w.

    >>> cross_product([], [2])
    [0, 0, 0]
    >>> cross_product([2, 8], [1, 4, 3])
    [24, -6, 0]
    >>> cross_product([1, 1, 1], [5.5, 5.5, 5.5])
    [0.0, -0.0, 0.0] 
    >>> cross_product( [1, 1, 1, 0], [1, 5.5])
    []

    '''
    if (len(v) > 3 or len(w) > 3):
        return []
    for x in range(len(v), 3):
        v.append(0)
    for x in range(len(w), 3):
        w.append(0)
    
    return ([v[1]*w[2]-v[2]*w[1]],[-(v[0]*w[2]-v[2]*w[0])],[v[0]*w[1]-v[1]*w[0]])

def scalar_projection(v,w):
    ''' 
    (List[int], List[int]) -> float

    Returns the scalar projection of w onto v.

    >>> scalar_projection([-2], [1.5])
    -1.5
    >>> scalar_projection([0, 3], [1.5, 2])
    2.0
    '''
    return(dot_product(v,w) / vector_length(v))

def vector_projection(v,w):
    ''' 
    (List[int], List[int]) -> float

    Returns the vector projection of w onto v.

    >>> vector_projection([-2], [1.5])
    [1.5]
    >>> vector_projection([0, 3], [1.5, 2])
    [0.0, 2.0]
    '''
    temp = (dot_product(v,w) / pow(vector_length(v),2))

    for x in range(0,len(v)):
        v[x] *= temp

    return v

if __name__ == "__main__":
    # test your vector operations here
    '''
    v1 = [0, -2, 3]
    v2 = [1, 1, 1]
    print(vector_from_points([0, 0], [1, 2]))
    print(vector_from_points([3, -1, 0], [10, 0, 1]))
    print(vector_length([2, 1]))
    print(vector_length([]))
    print(angle_between([-1], [2]))
    print(dot_product( [-1], [2]))
    print(dot_product( [0, 1, 0, 1], [1, 3, 4, 5]))
    print(dot_product([0, 0], [0, 0]))
    print(unit_vector([2, 1]))
    print(cross_product([], [2]))
    print(cross_product([2, 8], [1, 4, 3]))
    print(cross_product([1, 1, 1], [5.5, 5.5, 5.5]))
    print(cross_product( [1, 1, 1, 0], [1, 5.5]))
    print(scalar_projection([-2], [1.5]))
    print(scalar_projection([0, 3], [1.5, 2]))
    print(vector_projection([-2], [1.5]))
    print(vector_projection([0, 3], [1.5, 2]))
    '''
