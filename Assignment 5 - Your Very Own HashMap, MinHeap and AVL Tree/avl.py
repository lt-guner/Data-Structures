# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 5
# Description: This portion of the project deals with AVLs


import random


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self):
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self):
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self):
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return 'AVL Node: {}'.format(self.value)


class AVL:
    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate AVL with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if cur:
            values.append(str(cur.value))
            self._str_helper(cur.left, values)
            self._str_helper(cur.right, values)

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            node = s.pop()
            if node:
                # check for correct height (relative to children)
                l = node.left.height if node.left else -1
                r = node.right.height if node.right else -1
                if node.height != 1 + max(l, r):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                s.push(node.right)
                s.push(node.left)
        return True

    # -------------------------------------------- helper functions ---------------------------------------------------

    def contains(self, value: object) -> bool:
        """
        returns true or false if the element is in the tree
        """

        # set traverse to self.root
        traverse = self.root

        # traverse through the the tree until the value is found and return true else return false
        while traverse != None:
            if traverse.value == value:
                return True
            if value > traverse.value:
                traverse = traverse.right
            else:
                traverse = traverse.left

        return False

    def add_helper(self, value: object) -> bool:
        """
        Adds a value to an AVL (before balancing)
        """

        # if no root node, then assign new node as root
        if self.root == None:
            node = TreeNode(value)
            self.root = node
            return node

        # set traverse to self.root and iterate through until an self.right or self.left is available
        traverse = self.root

        while traverse.left != None or traverse.right != None:
            if value >= traverse.value:
                if traverse.right != None:
                    traverse = traverse.right
                else:
                    break
            else:
                if traverse.left != None:
                    traverse = traverse.left
                else:
                    break

        # a leaf is created and inserted self.right or self.left if is higher/same or lower than self.value respectively
        node = TreeNode(value)

        if traverse.value <= value:
            traverse.right = node
            node.parent = traverse
        else:
            traverse.left = node
            node.parent = traverse

        # return the node that was added
        return node

    def remove_helper(self, value) -> bool:
        """
        removes a value from an AVL (before balancing)
        """

        # return false if tree is empty
        if self.root == None:
            return False

        # set values to find the node with the value and the parent_node
        node = self.root
        parent_node = None

        # while loops until node is not none, and will break if the value is found
        while node != None:

            if value > node.value:
                parent_node = node
                node = node.right

            elif value < node.value:
                parent_node = node
                node = node.left

            elif value == node.value:
                break

        # if the node does not exist, then return False
        if node == None:
            return False

        # if the parent node is the value that is the node
        if parent_node == None:

            # if the root node has no left or right values then set to None
            if node.left == None and node.right == None:
                self.root = None

            # if right node is none, then left node is the new root
            elif node.right == None:
                self.root = node.left

            # if left node is none, then the right node is the root
            elif node.left == None:
                self.root = node.right

            # else we implement the processing updating the root node like it was an ordinary node
            else:

                # declare a successor and parent_successor
                successor = None
                parent_successor = None

                if node.right != None:
                    successor = node.right

                # loop until the successor is found and and its parent
                if successor != None:
                    while successor.left != None:
                        parent_successor = successor
                        successor = successor.left

                # update the node.value to the successor's value and update the parent_successor to point to the
                # successor child
                if parent_successor != None:
                    node.value = successor.value
                    parent_successor.left = successor.right
                    return parent_successor
                if parent_successor == None:
                    node.value = successor.value
                    node.right = successor.right
                    if node.right != None:
                        return node.right
                    else:
                        return node.left

            return parent_node

        # if it is a leaf node then set the parent to None
        if node.left == None and node.right == None:
            if parent_node.left == node:
                parent_node.left = None
            else:
                parent_node.right = None
            return parent_node

        # special cases for when there is only one branch attached to the node with the value
        # This case handles nodes on the right subtree
        if parent_node.right == node and ((node.right != None and node.left == None) or (node.left != None and node.right == None)):
            if node.right != None and node.left == None:
                parent_node.right = node.right
                node.right.parent = parent_node
                node.parent = None
                node.left = None
                node.right = None
            else:
                parent_node.right = node.left
                node.left.parent = parent_node
                node.parent = None
                node.left = None
                node.right = None
            return parent_node

        # This handles cases on the left subtree
        elif parent_node.left == node and ((node.right != None and node.left == None) or (node.left != None and node.right == None)):
            if node.right != None and node.left == None:
                parent_node.left = node.right
                node.right.parent = parent_node
                node.parent = None
                node.left = None
                node.right = None
            else:
                parent_node.left = node.left
                node.left.parent = parent_node
                node.parent = None
                node.left = None
                node.right = None
            return parent_node

        # if there are two children then the following code is used
        # declare a successor and parent_successor
        successor = node.right
        parent_successor = None

        # loop until the successor is found and and its parent
        while successor.left != None:
            parent_successor = successor
            successor = successor.left

        # update the node.value to the successor's value and update the parent_successor to point to the successor child
        if parent_successor != None:
            node.value = successor.value
            parent_successor.left = successor.right
            return parent_successor
        elif parent_node.value <= node.value:
            parent_node.right = successor
            successor.left = node.left
            node.left.parent = successor
            successor.parent = parent_node
            return successor
        else:
            parent_node.left = successor
            successor.left = node.left
            node.left.parent = successor
            successor.parent = parent_node
            node.parent = None
            node.left = None
            node.right = None
            return successor

        return parent_node

    def set_height(self, node):
        """
        The function updates the heights of nodes after insertion or deletion in the AVL tree
        """

        # --- pseudocode ---
        # updateHeight(N):
        #    N.height ← MAX(height(N.left), height(N.right)) + 1

        # declare both children as -1
        left_height = -1
        right_height = -1

        # if left child exists, update the left_height variable
        if node.left != None:
            left_height = node.left.height

        # if right child exists, update the right_height variable
        if node.right != None:
            right_height = node.right.height

        # update the height of the node
        node.height = max(right_height, left_height) + 1

        return

    def balance_factor(self, node):
        """
        returns the balance factor for node
        """

        # --- pseudocode ---
        # balanceFactor(N)
        #     return right.height - left.height

        # if both are none, return -1
        if node.left == None and node.right == None:
            return -1

        # if only left child is none, treat left node as -1
        elif node.left == None:
            return node.right.height - (-1)

        # if only right child is none, treat right child as -1
        elif node.right == None:
            return (-1) - node.left.height

        # else pass the balance factor from subtracting both heights
        else:
            return node.right.height - node.left.height

    def rotate_left(self,node):
        """
        The rotate_left method performs a left rotation around the N node, which brings up the C node and makes
        the N node the left child of the C. This method readjusts the heights of the altered nodes.
        """

        # --- pseudocode ---
        # rotateLeft(N):
        # C ← N.right
        # N.right ← C.left
        # if N.right is not NULL:
        #     N.right.parent ← N
        # C.left ← N
        # N.parent ← C
        # updateHeight(N)
        # updateHeight(C)
        # return C

        # declare nodes to rotate
        n_node = node
        c_node = node.right
        n_p_node = node.parent
        c_l_node = node.right.left
        direction = None

        # determine location whether n_code is the left or right child of the n_p_code if n_p_node is not none
        if n_p_node != None:
            if n_p_node.left == n_node:
                direction = "left"
            else:
                direction = "right"

        # swap the n and c nodes counter_clockwise
        c_node.left = n_node
        n_node.parent = c_node

        # update n_p_node and c_node connections
        c_node.parent = n_p_node
        if direction == "left":
            n_p_node.left = c_node
        elif direction == "right":
            n_p_node.right = c_node

        # update c_l_node and p_node
        n_node.right = c_l_node
        if c_l_node != None:
            c_l_node.parent = n_node

        # if c_node now has no parent, then set it as root
        if c_node.parent == None:
            self.root = c_node

        # update heights of the n and c nodes
        self.set_height(n_node)
        self.set_height(c_node)

        # return c_node
        return c_node

    def rotate_right(self, node):
        """
        The rotate_right method performs a right rotation around the N node, which brings up the C node and makes
        the N node the right child of the C. This method readjusts the heights of the altered nodes.
        """

        # --- pseudocode ---
        # rotateRight(N):
        # C ← N.left
        # N.left ← C.right
        # if N.left is not NULL:
        #     N.left.parent ← N
        # C.right ← N
        # N.parent ← C
        # updateHeight(N)
        # updateHeight(C)
        # return C

        # declare nodes to rotate
        n_node = node
        c_node = node.left
        n_p_node = node.parent
        c_r_node = node.left.right
        direction = None

        # determine location whether n_code is the left or right child of the n_p_code if n_p_node is not none
        if n_p_node != None:
            if n_p_node.left == n_node:
                direction = "left"
            else:
                direction = "right"

        # swap the n and c nodes counter_clockwise
        c_node.right = n_node
        n_node.parent = c_node

        # update n_p_node and c_node connections
        c_node.parent = n_p_node
        if direction == "left":
            n_p_node.left = c_node
        elif direction == "right":
            n_p_node.right = c_node

        # update c_l_node and p_node
        n_node.left = c_r_node
        if c_r_node != None:
            c_r_node.parent = n_node

        # if c_node now has no parent, then set it as root
        if c_node.parent == None:
            self.root = c_node

        # update heights of the n and c nodes
        self.set_height(n_node)
        self.set_height(c_node)

        # return c_node
        return c_node

    def rebalance(self, node):
        """
        The rebalance method performs a rebalancing of the AVL when a node is inserted or deleted from the AVL. It
        performs rotations and height adjustments on affected nodes.
        """

        # --- pseudocode ---
        # if balanceFactor(N) < -1:
        #     if balanceFactor(N.left) > 0:
        #         N.left ← rotateLeft(N.left)
        #         N.left.parent ← N
        #     newSubtreeRoot ← rotateRight(N)
        #     newSubtreeRoot.parent ← N.parent
        #     N.parent.left or N.parent.right ← newSubtreeRoot
        # else if balanceFactor(N) > 1:
        #     if balanceFactor(N.right) < 0:
        #         N.right ← rotateRight(N.right)
        #         N.right.parent ← N
        #     newSubtreeRoot ← rotateLeft(N)
        #     newSubtreeRoot.parent ← N.parent
        #     N.parent.left or N.parent.right ← newSubtreeRoot
        # else:
        #     updateHeight(N)

        # If the tree is left heavy proceed. If it is LR then perform a left rotation followed by right rotation, else
        # perform a standard right rotatiion
        if self.balance_factor(node) < -1:
            if self.balance_factor(node.left) > 0:
                n_temp = self.rotate_left(node.left)
                self.rotate_right(n_temp.parent)
            else:
                self.rotate_right(node)

        # If the tree is right heavy proceed. If it is RL then perform a right rotation followed by left rotation, else
        # perform a standard left rotation
        elif self.balance_factor(node) > 1:
            if self.balance_factor(node.right) < 0:
                n_temp = self.rotate_right(node.right)
                self.rotate_left(n_temp.parent)
            else:
                self.rotate_left(node)

        # if no rotation needed then just adjust height
        else:
            self.set_height(node)

        return

    # ---------------------------------------- assignment functions ---------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a node to the AVL tree. It does so in O(LogN) time by first inserting the node into the AVL as if it was
        an ordinary BST, and then only performing height adjustments needed on affected nodes in the subtrees rotations.
        """

        # --- pseudocode --
        # avlInsert(tree, key, value):
        #     insert key, value into tree like normal BST insertion
        #     N ← newly inserted node
        #     P ← N.parent
        #     while P is not NULL:
        #         rebalance(P)
        #         P ← P.parent

        # check if right value is already in the node and do nothing if the node exists
        if self.contains(value) == True:
            return

        # store node in the tree like as it was for a normal BST
        node = self.add_helper(value)
        parent = 0

        # if node.parent is not None assign to parent else return
        if node.parent != None:
            parent = node.parent
        else:
            return

        # while through parent to balance the avl up to root
        while parent != None:
            self.rebalance(parent)
            parent = parent.parent

        return

    def remove(self, value: object) -> bool:
        """
        The remove method removes a node from an AVL. It does so in O(LogN) time by first deleting the node from the
        AVL as if it was an ordinary BST, and then only performing height adjustments needed on affected nodes in the
        subtrees rotations.
        """

        # --- psedocode ---
        # avlRemove(tree, key):
        #     remove key from tree like normal BST removal
        #     P ← lowest modified node (e.g. parent of removed node)
        #     while P is not NULL:
        #         rebalance(P)
        #         P ← P.parent

        # remove the node and save the parent node
        parent = self.remove_helper(value)

        # if there is no parent node then return false because value is not found
        if parent == False:
            return False

        # while loop to adjust height with balance method
        while parent != None:
            self.rebalance(parent)
            parent = parent.parent

        # return True when complete
        return True

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':
    """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        avl = AVL(case)
        print(avl)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        avl = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', avl)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        avl = AVL()
        for value in case:
            avl.add(value)
        if not avl.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')
    

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    avl = AVL(case)
    for del_value in case:
        print('INPUT  :', avl, del_value)
        avl.remove(del_value)
        print('RESULT :', avl)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    avl = AVL(case)
    for _ in case[:-2]:
        print('INPUT  :', avl, avl.root.value)
        avl.remove(avl.root.value)
        print('RESULT :', avl)
    """

    print("\nTimur Guner")
    print("-------------------------------")
    avl = AVL([-59,-64,33,-80,-63,9,72,-85,-70,61])
    print(avl)
    avl.remove(-64)
    print(avl)

    if not avl.is_valid_avl():
        raise Exception("PROBLEM WITH REMOVE OPERATION")
    else:
        print("passed")


    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        avl = AVL(case)
        for value in case[::2]:
            avl.remove(value)
        if not avl.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')
