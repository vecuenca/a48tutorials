def sorted_kroy_list_insert(head, newnum):
        """ (KroyNode, int) -> KroyNode

        Move the second node in the linked list with first node head to the second last position in the list.
        Return the data in the moved node.
        REQ: The linked list with first node head has at least 3 nodes.
        """
        newnode = KroyNode(newnum)
        if head == None:
            # restore stolen code here
            head = newnode                      # ----

        elif newnum < head.number:
            # restore stolen code here
            newnode.next1 = head                # ----
            newnode.next2 = head.next1          # ----
            head = newnode                      # ----

        else:
            prev = head
            curr = head.next1
            while curr != None and curr.number <= newnum:
                if curr.next1 != None and curr.next1.number > newnum:
                    # restore stolen code here
                    prev.next2 = newnode        # ----
                prev = curr
                curr = curr.next1
            # restore stolen code here
            prev.next1 = newnode                # ----

            if curr != None:
                # restore stolen code here
                prev.next2 = curr               # ----
                newnode.next1 = curr            # ----
                newnode.next2 = curr.next1      # ----

        return head
