class DLLNode(object):
    """A Node in a doubly-linked list"""
    
    def __init__(self, data, prev_link=None, next_link=None):
        '''(DLLNode, object, DLLNode, DLLNode) -> NoneType

        Create a new DLLNode containing object, with previous node
        prev_link, and next node next_link.
        '''
        # Representation invariant:
        # data is an object
        # prev_link is a DLLNode
        # next_link is a DLLNode
        # data is the item held in this node
        # prev_link is the node immediately before (closer 
        # to the head of the list than) this node
        # next_link is the node immediately after (closer
        # to the tail of the list than) this node

        self.data = data
        self.prev_link = prev_link
        self.next_link = next_link
    
    def __str__(self):
        '''(DLLNode) -> str
        Return a str representation of this DLLNode.
        '''

        return str(self.data)
    
class DoublyLinkedList(object):
    """A doubly linked list"""
    
    def __init__(self):
        '''(DoublyLinkedList) -> NoneType
        Create a new empty DoublyLinkedList
        '''
        # Representation invariant:
        # _head is a DLLNode
        # _tail is a DLLNode
        # if the list is empty:
        #     _head = _tail = None
        # if the list is non-empty:
        #     _head is the first node in the list
        #     _tail is the last node in the list
        #     if nodeA and nodeB are both nodes in this list and nodeA is
        #     before (closer to the head than) nodeB:
        #         nodeA.next_link[.next_link]* = nodeB
        #             ([.next_link]* = 0 or more repetitions of .next_link)
        #         nodeB.prev_link[.prev_link]* = nodeA
        self._head = None
        self._head = None
        
    def __str__(self):
        '''(DoublyLinkedList) -> str
        
        Return a str representation of the contents of this
        DoublyLinkedList.
        '''
        dll_str = ""
        cur_node = self._head
        while cur_node is not None:
            dll_str += str(cur_node.data) + "<->"
            cur_node = cur_node.next_link
        return dll_str

    def add_head(self, add_obj):
        '''(DoublyLinkedList, object) -> NoneType
        Add add_obj to the head of this DoublyLinkedList.
        '''
        # two cases: this DLL is empty,
        # or there is an existing head to append onto

        if self._head:
            self._head.prev_link = DLLNode(add_obj, None, self._head)
            self._head = self._head.prev_link
        else:
            new_node = DLLNode(add_obj, None, None)
            self._head = new_node
            self._tail = new_node


    
    def add_tail(self, add_obj):
        '''(DoublyLinkedList, object) -> NoneType
        Add add_obj to the tail of this DoublyLinkedList.
        '''
        # again, two cases: empty DLL, or existing tail to append onto
        if self._tail:
            self._tail.next_link = DLLNode(add_obj, self._tail, None)
            self._tail = self._tail.next_link
        else:
            new_node = DLLNode(add_obj, None, None)
            self._head = new_node
            self._tail = new_node
    
    def add_index(self, add_obj, add_index):
        '''(DoublyLinkedList, object, int) -> NoneType
        Add add_obj to this DoublyLinkedList at index add_index.
        '''

        if self._head == self._tail or add_index == 0:
            self.add_head(add_obj)
        else:
            # start at the head, and traverse the DLL until we find the right index
            # to insert our new node
            i = 0
            insert_node = self._head

            while i != add_index - 1:
                insert_node = insert_node.next_link
                i += 1

            new_node = DLLNode(add_obj)
            new_node.prev_link = insert_node
            new_node.next_link = insert_node.next_link

            if insert_node.next_link is None:
                self._tail = new_node
            else:
                insert_node.next_link.prev_link = new_node
            insert_node.next_link = new_node

    
    def remove_head(self):
        '''(DoublyLinkedList) -> object
        Remove and return the first item in this DoublyLinkedList.
        '''
        # two cases:
        item = self._head.data
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next_link
            self._head.prev_link = None
        return item
        
    def remove_tail(self):
        '''(DoublyLinkedList) -> object
        Remove and return the last item in this DoublyLinkedList.
        '''
        if self._head == self._tail:
            item = self._head.data
            self._head = self._tail = None
            return item
        else:
            item = self._tail.data
            self._tail = self._tail.prev_link
            self._tail.next_link = None
            return item

    def remove_index(self, remove_index):
        '''(DoublyLinkedList, int) -> object
        
        Remove and return the item at index remove_index in this
        DoublyLinkedList.
        '''
        if self._head == self._tail or remove_index == 0:
            return self.remove_head()
        else:
            i = 0
            remove_node = self._head

            while i != remove_index - 1:
                remove_node = remove_node.next_link
                i += 1

            item = remove_node.next_link.data


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.add_head('A')
    dll.add_head('B')
    dll.add_head('C')
    dll.add_index('D', 0)

    print(dll)
    print(dll._head)
    print(dll._tail)


