class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0  # the depth of this node in a tree
        self.sibling = False

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + str(self.sibling) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def get_height(self):
        '''(BTNode) -> int
        Return the height of the tree rooted at this node. We define the
        height of a tree with a single node to be 1
        '''
        left_height = 0
        right_height = 0

        if(self.left):
            left_height = self.left.get_height()

        if(self.right):
            right_height = self.right.get_height()

        return max(left_height, right_height) + 1

    def set_sibling(self, have_sib=False):
        '''(BTNode[, bool]) -> NoneType
        For each node in the tree rooted at this node, set their
        .sibling variable to True iff they have a sibling
        '''
        self.sibling = have_sib
        if(self.left and self.right):
            self.left.set_sibling(True)
            self.right.set_sibling(True)
        elif(self.left):
            self.left.set_sibling(False)
        elif(self.right):
            self.right.set_sibling(False)




if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))
    print(my_tree)
    my_tree.set_sibling()
    print(my_tree)

    print('Height of my tree: ' + str(my_tree.get_height()))
