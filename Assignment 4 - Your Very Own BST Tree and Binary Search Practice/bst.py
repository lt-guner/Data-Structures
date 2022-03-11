# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 4
# Description: Assignment 4 implements binary search tress and the methods to manipulate them


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

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
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

    def dequeue(self) -> object:
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
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # -------------------------------Helper Methods for CS261 Assignment 4------------------------------------------- #

    def pre_order_rec(self, traverse, preorder) -> Queue:
        """
        This method is a recursive helper function for pre_order_traversal to help build the queue
        """

        # add the element to the queue
        preorder.enqueue(traverse.value)

        # visit left subtree if it exists
        if traverse.left != None:
            self.pre_order_rec(traverse.left, preorder)

        # visit right subtree if it exists
        if traverse.right != None:
            self.pre_order_rec(traverse.right, preorder)

        return

    def in_order_rec(self, traverse, inorder) -> Queue:
        """
        This method is a recursive helper function for in_order_traversal to help build the queue
        """

        # visit left subtree if it exists
        if traverse.left != None:
            self.in_order_rec(traverse.left, inorder)

        # add the element to the inorder queue
        inorder.enqueue(traverse.value)

        # visit right subtree if it exists
        if traverse.right != None:
            self.in_order_rec(traverse.right, inorder)

        return

    def post_order_rec(self, traverse, postorder) -> Queue:
        """
        This method is a recursive helper function for post_order_traversal to help build the queue
        """

        # visit left subtree if it exists
        if traverse.left != None:
            self.post_order_rec(traverse.left,postorder)

        # visit right subtree if it exists
        if traverse.right != None:
            self.post_order_rec(traverse.right,postorder)

        # add element to the postorder queue
        postorder.enqueue(traverse.value)

        return

    def height_rec(self, traverse) -> int:
        """
        a recursive helper method for height(), which helps counts the number of edges
        """

        # if current traverse is none, return -1
        if traverse == None:
            return -1

        # recursively call height_rec for height of left and right subtrees
        left_tree_height = self.height_rec(traverse.left)
        right_tree_height = self.height_rec(traverse.right)

        # the max height of the two subtrees is returned + 1, since it count the number of edges
        if right_tree_height >= left_tree_height:
            return right_tree_height + 1
        else:
            return left_tree_height + 1


    def size_rec(self, traverse) -> int:
        """
        a recursive helper method for size(), which helps count the number of nodes
        """

        # if current traverse is none, return 0
        if traverse == None:
            return 0

        # recursively call size_rec for size of left and right subtrees
        left_tree_size = self.size_rec(traverse.left)
        right_tree_size = self.size_rec(traverse.right)

        # add the size of the two subtrees together plus one for the current node to find the current size of the BST
        return left_tree_size + right_tree_size + 1

    def leaves_rec(self, traverse):
        """
        a recursive helper method for count_leaves() to help count the leaves
        """

        # if a leave node is found return 1 to count it as a leaf
        if traverse.left == None and traverse.right == None:
            return 1

        # declare variables to store the counts of leaves for left and right subtrees
        left_tree = 0
        right_tree = 0

        # if traverse.left contains a node, recursively call the leaves_rec and saves the count of leaves in left_tree
        if traverse.left != None:
            left_tree = self.leaves_rec(traverse.left)

        # if traverse.right contains a node, recursively call leaves_rec and save the count of leaves in right_tree
        if traverse.right != None:
            right_tree = self.leaves_rec(traverse.right)

        # return the leaves of left and right tree
        return left_tree + right_tree

    def unique_rec(self, traverse, inorder_stack) -> Queue:
        """
        This method is a recursive helper function for count_unique to help build the stack
        """

        # visit left subtree if it exists
        if traverse.left != None:
            self.unique_rec(traverse.left, inorder_stack)

        # add the element to the inorder_stack with a push
        inorder_stack.push(traverse.value)

        # visit right subtree if it exists
        if traverse.right != None:
            self.unique_rec(traverse.right, inorder_stack)

        return

    def is_full_rec(self,traverse):
        """
        helper method of is_full() to help determine if the tree is a full binary tree
        """

        # if only the right or left of node is none, return false
        if (traverse.left != None and traverse.right == None) or (traverse.left == None and traverse.right != None):
            return False

        # recursively traverse the left tree and return False if left_tracker captured false
        if traverse.left != None:
            left_tracker = self.is_full_rec(traverse.left)
            if left_tracker == False:
                return False

        # recursively traverse the right tree and return False if the right_tracker captured false
        if traverse.right != None:
            right_tracker = self.is_full_rec(traverse.right)
            if right_tracker == False:
                return False

        # return true is False was not found
        return True

    # --------------------------------------Methods CS261 Assignment 4----------------------------------------------- #

    def add(self, value: object) -> None:
        """
        Adds a value to a binary search tree
        """

        # create a root node if the value tree is empty
        if self.root == None:
            node = TreeNode(value)
            self.root = node
            return

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
        else:
            traverse.left = node

        return

    def contains(self, value: object) -> bool:
        """
        returns true or false if the element is in the tree
        """

        # returns false if root is none
        if self.root == None:
            return False

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

    def get_first(self) -> object:
        """
        returns the root of the tree or returns none if tree is empty
        """

        if self.root == None:
            return None

        return self.root.value

    def remove_first(self) -> bool:
        """
        removes the first node in the tree
        """

        if self.root == None:
            return False
        else:
            self.remove(self.root.value)

        return True

    def remove(self, value) -> bool:
        """
        removes the node and returns true if the value is present, else removes false
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
                if parent_successor == None:
                    node.value = successor.value
                    node.right = successor.right

            return True

        # if it is a leaf node then set the parent to None
        if node.left == None and node.right == None:
            if parent_node.left == node:
                parent_node.left = None
            else:
                parent_node.right = None
            return True

        # special cases for when there is only one branch attached to the node with the value
        # This case handles nodes on the right subtree
        if parent_node.right == node and ((node.right != None and node.left == None) or (node.left != None and node.right == None)):
            if node.right != None and node.left == None:
                parent_node.right = node.right
            else:
                parent_node.right = node.left
            return True

        # This handles cases on the left subtree
        elif parent_node.left == node and ((node.right != None and node.left == None) or (node.left != None and node.right == None)):
            if node.right != None and node.left == None:
                parent_node.left = node.right
            else:
                parent_node.left = node.left
            return True

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
        elif parent_node.value <= node.value:
            parent_node.right = successor
            successor.left = node.left
        else:
            parent_node.left = successor
            successor.left = node.left

        return True

    def pre_order_traversal(self) -> Queue:
        """
        The method returns a queue that contains the pre-order traversal of nodes visited
        """

        # create a queue and a pointer to the tree
        preorder = Queue()
        traverse = self.root

        # return blank queue if root is empty
        if self.root == None:
            return preorder

        # call the helper function to recursively fill the call
        self.pre_order_rec(traverse, preorder)

        # return the queue
        return preorder

    def in_order_traversal(self) -> Queue:
        """
        The method returns a queue that contains the in-order traversal of nodes visited
        """

        # create a queue and a pointer to the tree
        inorder = Queue()
        traverse = self.root

        # return blank queue if root is empty
        if self.root == None:
            return inorder

        # call the helper function to recursively fill the call
        self.in_order_rec(traverse,inorder)

        # return the queue
        return inorder

    def post_order_traversal(self) -> Queue:
        """
        The method returns a queue that contains the post-order traversal of nodes visited
        """

        # create a queue and a pointer to the tree
        postorder = Queue()
        traverse = self.root

        # return blank queue if root is empty
        if self.root == None:
            return postorder

        # call the helper function to recursively fill the call
        self.post_order_rec(traverse,postorder)

        # return the queue
        return postorder

    def by_level_traversal(self) -> Queue:
        """
        The method returns a queue that of traversal of binary search tree by level or breadth search
        """

        # create a tempqueue and breadth queue to return to the user, as well as enqueue the root node
        tempqueue = Queue()
        breadth = Queue()

        # return empty queue root is blank
        if self.root == None:
            return tempqueue

        tempqueue.enqueue(self.root)

        # The while loop uses tempqueue to store and pop nodes. A node is dequeued from tempqueue and the value is
        # enqueued in breadth and its child nodes in equeued in tempqueue. This solution stores the data in breadth
        # by level  traversal and the loop completes
        while tempqueue.is_empty() != True:
            tempnode = tempqueue.dequeue()
            breadth.enqueue(tempnode.value)
            if tempnode.left != None:
                tempqueue.enqueue(tempnode.left)
            if tempnode.right != None:
                tempqueue.enqueue(tempnode.right)        

        # return breadth
        return breadth

    def is_full(self) -> bool:
        """
        Returns true if the tree is a full binary tree, else returns false. A full binary tree is a binary tree in which
        every interior node has exactly two children.
        """

        # return true if BST is empty
        if self.root == None:
            return True

        # assign self.root to traverse
        traverse = self.root

        # call the recursive function to determine if it is a full binary tree and safe value in is_full_value
        is_full_value = self.is_full_rec(traverse)

        # is_full_value will be either true or false
        return is_full_value

    def is_complete(self) -> bool:
        """
        Returns true if the tree is a complete binary tree, else returns false. A complete binary tree is a binary tree
        that is perfect except for the deepest level, whose nodes are all as far left as possible.
        """

        # create tempqueue to keep track of level traversal and a node_flag to determine
        tempqueue = Queue()
        node_flag = False

        # return True if queue is empty
        if self.root == None:
            return True

        # add the root to the tempqueue
        tempqueue.enqueue(self.root)

        # The while loop works like the by_level_traversal. The loop continues until the loop is empty or false is
        # returned. It loops through until it finds a node that none full node is found and variable is True. Moving
        # forward, if there are nodes that pass a node marked node by position or depth, then the node_flag would cause
        # the function to return False.
        while tempqueue.is_empty() != True:
            node_holder = tempqueue.dequeue()
            if node_holder.left != None:
                if node_flag == True:
                    return False
                tempqueue.enqueue(node_holder.left)
            else:
                node_flag = True
            if node_holder.right != None:
                if node_flag == True:
                    return False
                tempqueue.enqueue(node_holder.right)
            else:
                node_flag = True

        # return true if while loop is complete
        return True

    def is_perfect(self) -> bool:
        """
        Returns true if the tree is a perfect binary tree, else returns false. A perfect binary tree is a full binary
        tree (i.e. one where all interior nodes have two children) where all the leaves are at the same depth.
        """

        # find the height and leaves of the BST
        height = self.height()
        leaves = self.count_leaves()

        # if height is -1 return true
        if height == -1:
            return True

        # if it is a perfect binary tree, then the number of leaves = 2^(height)
        if (2**height) == leaves:
            return True

        # return false if it did not pass the formula for if statement
        return False

    def size(self) -> int:
        """
        returns the number of nodes in the binary search tree
        """

        # if root is none, then size is 0
        if self.root == None:
            return 0

        # set root to traverse and call size_rec to find the height
        traverse = self.root
        size = self.size_rec(traverse)

        return size

    def height(self) -> int:
        """
        returns the height of the binary search tree (maximum depth)
        """

        # if tree is empty, return -1
        if self.root == None:
            return -1

        # assign self.root to traverse and use the height_rec() to find height
        traverse = self.root
        height = self.height_rec(traverse)

        # return height
        return height

    def count_leaves(self) -> int:
        """
        The function counts the number of leaves and returns it
        """

        # if the bst is empty, return 0
        if self.root == None:
            return 0

        # assign root to traverse and save the count of leaves from the recursive call to leaves_rec in leaves
        traverse = self.root
        leaves = self.leaves_rec(traverse)

        # return leaves
        return leaves

    def count_unique(self) -> int:
        """
        counts the number of unique nodes in the BST
        """

        # if BST is empty, then return 1
        if self.root == None:
            return 0

        # set counter to 0, create a stack, and set root to traverse
        count_unique = 0
        inorder_stack = Stack()
        traverse = self.root

        # call the recursive function unique_rec to built a stack in inorder_stack
        self.unique_rec(traverse,inorder_stack)

        # Loop through and compare the current top value on stack to the recent popped value and increment count_unique
        # if the values are not the same. Continue popping and comparing until the stack is empty
        curr = inorder_stack.pop()
        if inorder_stack.is_empty() != True:
            while inorder_stack.is_empty() != True:
                if curr != inorder_stack.top():
                    count_unique+=1
                curr = inorder_stack.pop()
            count_unique+=1
        else:
            count_unique+=1

        # return count_unique
        return count_unique

# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST(['QV', 'L', 'CO', 'H', 'L', 'N', 'N', 'UY', 'S', 'XY'])
    print(tree.remove('L'))
    print(tree)
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST(['PI', 'O', 'AE', 'K', 'Q', 'PI', 'Y'])
    print(tree.remove('Q'))
    print(tree)
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([-9, 3, -9, 2, -8, -2, -2, 2, 6, 4])
    print(tree.remove(2))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

