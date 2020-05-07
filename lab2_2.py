def packet_size(packet):
    ''' 
    (List[int]) -> int

    Returns the size of the packet in bits.

    >>> packet_size([0,1,0,1])
    4
    >>> packet_size([1,1,1])
    3
    '''
    return len(packet)

def error_indices(packet1, packet2):
    ''' 
    (List[int]) -> List[int]

    Returns a list indicating all the indices where packet1 and packet2 are different.

    >>> error_indices([0,1,1,1], [1,1,0,1])
    [0, 2]
    >>> error_indices([1,1,0,1], [1,1,0,1])
    []
    '''
    mistakes = []
    for x in range(0, len(packet1)):
        if(packet1[x] != packet2[x]):
            mistakes.append(x)
    return mistakes

def packet_diff(packet1, packet2):
    '''
    (List[int], List[int]) -> int

    Returns the number of differences between packet1 and packet2.

    >>> packet_diff([0,1,0,1], [1,1,0,1])
    1
    >>> packet_diff([0,1,1,0], [0,1,1,0])    
    0
    '''
    return len(error_indices(packet1, packet2))

if __name__ == "__main__":
    # test your bit error rate detector here
    packet_sent = [0, 1, 1, 1]
    packet_received = [1, 1, 1, 1]
    print(packet_size([0,1,0,1]))
    print(error_indices([0,1,1,1], [1,1,0,1]))
    print(error_indices([1,1,0,1], [1,1,0,1]))
    print(packet_diff([0,1,0,1], [1,1,0,1]))
    print(packet_diff([0,1,1,0], [0,1,1,0]))
