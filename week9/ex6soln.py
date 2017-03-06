def rsum(lst):
    ''' (list of ints) -> int
    returns the sum of all elements in this list (at any nesting level).
    '''
    # base case
    if lst == []:
        return 0
    # get sum of nested list, add it with sum of rest of the list
    elif isinstance(lst[0], list):
        return rsum(lst[0]) + rsum(lst[1:])
    # sum current element with rest of list
    else:
        return lst[0] + rsum(lst[1:])

def rmax(lst):
    ''' (list of ints) -> int
    returns the max number in this list (at any nesting level)
    '''
    return _rmax_helper(lst, 0)

def _rmax_helper(lst, cur_max):
    # base case, return the max number we have seen so far
    if lst == []:
        return cur_max

    # get max of nested list
    if isinstance(lst[0], list):
        max = _rmax_helper(lst[0], cur_max)
    # otherwise get current element to compare with cur_max
    else:
        max = lst[0]

    # recursive call
    if max > cur_max:
        return _rmax_helper(lst[1:], max)
    else:
        return _rmax_helper(lst[1:], cur_max)

def second_smallest(lst):
    return _second_smallest_helper(lst, (float('inf'), float('inf')))[1]

def _second_smallest_helper(lst, two_smallest):
    '''
    returns the two smallest elements in this list
    '''
    # base case, return the two_smallest we have seen so far
    if lst == []:
        return two_smallest

    if isinstance(lst[0], list):
        # get two smallest of nested list
        nested_smallest = _second_smallest_helper(lst[0], (float('inf'), float('inf')))
        # update two_smallest tuple if needed
        two_smallest = _update_smallest(two_smallest, nested_smallest[0])
        two_smallest = _update_smallest(two_smallest, nested_smallest[1])
    else:
        # update two_smallest with current element if needed
        two_smallest = _update_smallest(two_smallest, lst[0])
    return _second_smallest_helper(lst[1:], two_smallest)

def _update_smallest(two_smallest, num):
    '''
    updates the two_smallest tuple if num is smaller than either nums in the tuple
    two_smallest is ordered, i.e. two_smallest[0] < two_smallest[1]
    '''
    # case 1: num is the smallest out of all 3 nums
    # two_smallest[0] should be shifted over one
    if num < two_smallest[0] and num < two_smallest[1]:
        two_smallest = (num, two_smallest[0])
    # case 2: num is smaller than index 1, but not index 0
    elif num < two_smallest[1]:
        two_smallest = (two_smallest[0], num)
    return two_smallest

def two_smallest(my_list):
    """ (list of int) -> tuple of (int, int)
    CREDIT: Cho Yin Yong
    Given a list of integers, return the two smallest numbers in the list
    as a tuple of (int, int)

    REQ: len(my_list) >= 1

    >>> two_smallest([[1, 2], [2, [3]], []])
    (1, 2)
    >>> two_smallest([1, 2, [2, 3]])
    (1, 2)
    >>> two_smallest([4, 1, 1, 3])
    (1, 1)
    >>> two_smallest([[], 1, 1, []])
    (1, 1)
    >>> two_smallest([1, [1, 3, [[[[[3, 4]]]]]]])
    (1, 1)
    >>> two_smallest([[3], [], 3])
    (3, 3)
    >>> two_smallest([[[[2, 2]]]])
    (2, 2)
    >>> two_smallest([[], [], 2, 10])
    (2, 10)
    >>> two_smallest([0, 0, 0, [], []])
    (0, 0)
    >>> two_smallest([[],[[3, 4]]])
    (3, 4)
    >>> two_smallest([[],[3, 4]])
    (3, 4)
    """
    # dummy var to return tuple
    smallest_tuple = tuple()

    # if first element is a list, go in the list
    if isinstance(my_list[0], list):
        smallest_tuple = two_smallest(my_list[0] + my_list[1:])

    # if first element is not a list
    else:

        # second element is a list
        if isinstance(my_list[1], list):
            smallest_tuple = two_smallest(my_list[:1] +
                                          my_list[1] +
                                          my_list[2:])

        # length of list is two
        elif len(my_list) == 2:

            # smallest number goes first
            if my_list[0] > my_list[1]:
                smallest_tuple = (my_list[1], my_list[0])
            else:
                smallest_tuple = (my_list[0], my_list[1])

        # length of list is not 2
        else:

            # if the third element is a list, decompose it
            if isinstance(my_list[2], list):
                smallest_tuple = two_smallest(my_list[:2] +
                                              my_list[2] +
                                              my_list[3:])
            # if third element is int
            else:

                # remove biggest element
                if (my_list[0] > my_list[1] and
                    my_list[0] > my_list[2]):
                    smallest_tuple = two_smallest(my_list[1:])

                elif (my_list[1] > my_list[0] and
                      my_list[1] > my_list[2]):
                    smallest_tuple = two_smallest(my_list[:1] +
                                                  my_list[2:])
                else:
                    smallest_tuple = two_smallest(my_list[:2] +
                                                  my_list[3:])

    return smallest_tuple


if(__name__ == "__main__"):
    print(rsum([1,2,3, [1, [100, []], 2, 3]]))
    print(rmax([100,1,2,3,4,600,[1000,[],[12313123,666666666]],6]))
    print(second_smallest([2,1,[0, [5,6,[]]]]))