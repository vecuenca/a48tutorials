class EmptyQueueException(Exception):
    '''

    '''

class Deque():
    '''
    A Queue that can be en/dequeued from both ends.

    Uses a list to store the contents.
    '''

    def __init__(self):
        # representation invariant
        # _contents is a list of objects
        # _contents[:] represent the items in this deque
        # for i, j, where i >= 0, j < len(_contents)
        # if i < j: _contents[i] is left of _contents[j] in this deque
        self._contents = []

    def enqueue_left(self, item):
        ''' (Deque, object) -> None
        Insert an object at the far left side of this Deque.
        '''
        self._contents = [item] + self._contents

    def enqueue_right(self, item):
        self._contents += [item]

    def dequeue_left(self):
        ''' (Deque) -> object
        Remove and return the leftmost object in this Deque.
        '''
        if self.size() == 0:
            raise EmptyQueueException('cant dequeue from empty deque')
        return self._contents.pop(0)

    def dequeue_right(self):
        if self.size() == 0:
            raise EmptyQueueException('cant dequeue from empty deque')
        return self._contents.pop()

    def size(self):
        return len(self._contents)

def is_palindrome(word):
    ''' (string) -> bool
    Returns true if word is a palindrome, false o.w.
    dod and mom are palindromes, cat is not

    Implemented using a Deque.
    '''

    dq = Deque()

    for letter in word:
        dq.enqueue_right(letter)

    is_pal = True

    while dq.size() > 1 and is_pal:
        l = dq.dequeue_left()
        r = dq.dequeue_right()

        if l != r:
            is_pal = False

    return is_pal

if __name__ == '__main__':

    print(is_palindrome('wow'))

    print(is_palindrome('aaaaaab'))

    dq = Deque()

    dq.enqueue_left('A')
    dq.enqueue_left('B')
    dq.enqueue_left('C')
    dq.enqueue_right('D')
    dq.enqueue_right('E')
    dq.enqueue_right('F')

    while dq.size() > 0:
        print(dq.dequeue_left())
        print(dq.dequeue_right())

    # expected output: ABCFED or CBADEF or FAEBDC or CFBEAD?





