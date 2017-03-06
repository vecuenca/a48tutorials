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


if(__name__ == "__main__"):
    print(rsum([1,2,3, [1, [100, []], 2, 3]]))
    print(rmax([100,1,2,3,4,600,[1000,[],[12313123,666666666]],6]))
    print(second_smallest([2,1,[0, [5,6,[]]]]))