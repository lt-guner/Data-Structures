# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 3
# Description: This portion of assignment 3 implements the data structure of singly linked lists for bags and deques


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # -------------------------helper methods------------------------------------------------- #

    def add_back_helper(self, value, cur = None):
        """
        add_back_helper helps the add_back method to recursively add nodes to the end of the linked list
        """

        # recursively call the add_back_helper method until cur.next is self.tail and then add the new node
        if cur.next != self.tail:
            self.add_back_helper(value, cur.next)
        else:
            cur.next = SLNode(value)
            cur.next.next = self.tail

        return

    def remove_back_helper(self, cur = None):
        """
        remove_back_helper helps the remove_back method to recursively add nodes to the end of the linked list
        """

        # recursively call the add_back_helper method until cur.next is self.tail and then add the new node
        if cur.next.next == self.tail:
            cur.next = self.tail
        else:
            self.remove_back_helper(cur.next)

        return

    def get_back_helper(self, cur = None):
        """
        the get_back_helper method is recursively used by get_back to get the value from the last node
        """

        # recursively call the get_back_helper until cur.next is self.tail and pull the cur.value
        if cur.next == self.tail:
            return cur.value
        else:
            return self.get_back_helper(cur.next)

    def insert_at_index_helper(self, slot, index, value, cur = None):
        """
        The method is a recursive helper method for insert_at_index that is used to insert at a specific index
        """

        # if the slot is less than the desired index - 1, then recursively call insert_at_index_helper
        if slot < index - 1:
            slot += 1
            self.insert_at_index_helper(slot, index, value, cur.next)

        # else insert at the desired index
        else:
            temp = cur.next
            cur.next = SLNode(value)
            cur.next.next = temp

        return

    def remove_at_index_helper(self, slot, index, cur):
        """
        This is a recursive helper function to remove the node at the desired index for remove_at_index
        """

        # recursively call the function until the correct node is found and then set cur.next to cur.next.next
        if slot < index - 1:
            slot += 1
            self.remove_at_index_helper(slot, index, cur.next)
        else:
            cur.next = cur.next.next

        return

    def count_helper(self, count, value, cur):
        """
        a helper method for count that recursively counts the input value
        """

        # a recursive call the counts the elements in the list of the value that is passed.
        if cur.value != None:
            if cur.value == value:
                count+=1
            return self.count_helper(count, value, cur.next)

        return count

    def remove_helper(self, value, cur):
        """
        This is a recursive helper function to remove a node that contains the value and helps method remove
        """

        # recursively call the function until the correct node is found and then set cur.next to cur.next.next
        if cur.value != None:
            if cur.next.value == value:
                cur.next = cur.next.next
                return True
            else:
                return self.remove_helper(value, cur.next)

        # return false if not found
        return False

    def slice_helper(self, node_tracker, start_index, size, new_sll_nodes, new_sll_tail, cur):
        """
        This is helper function to slice node_tracker, start_index, size, new_sll.head, new_sll, self.head.next
        """

        # recursively call slice helper until the node_tracker = tart_index and on correct node from cur
        if node_tracker < start_index:
            return self.slice_helper(node_tracker+1, start_index, size, new_sll_nodes, new_sll_tail, cur.next)

        # recursively call the slice helper until size is 0, which means all values from cur are in equivalent nodes in
        # new_sll
        else:
            if size > 0:
                newNode = SLNode(cur.value)
                new_sll_nodes.next = newNode
                new_sll_nodes.next.next = new_sll_tail
                return self.slice_helper(node_tracker+1, start_index, size-1,new_sll_nodes.next,new_sll_tail,cur.next)

        return

    # ------------------------methods for assignment------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds a node to the front of the this
        """

        # if list is empty insert data and have it linked to both sentinels
        if self.is_empty() == True:
            newNode = SLNode(value)
            self.head.next = newNode
            self.head.next.next = self.tail

        # if there is node after the front sentinel, then insert after front sentinel and and link the chain
        else:
            newNode = SLNode(value)
            temp = self.head.next
            self.head.next = newNode
            self.head.next.next = temp

        return

    def add_back(self, value: object) -> None:
        """
        This method adds a note to the end of the list
        """

        # if list is empty, call add_front
        if self.is_empty() == True:
            self.add_front(value)

        # add to the back before the back sentinel
        else:
            self.add_back_helper(value, self.head.next)

        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new node with the passed value into the index specified by the user
        """

        # If the index is out of bounds, raise an exception flag
        if index < 0 or index > self.length():
            raise SLLException()

        # call add_front if index is 0
        elif index == 0:
            self.add_front(value)

        # else call insert_at_index_helper to recursively insert into the list
        else:
            slot = 0
            self.insert_at_index_helper(slot, index,value,self.head.next)

        return

    def remove_front(self) -> None:
        """
        Removes a node from the front
        """

        # raise exception if the list is empty
        if self.is_empty() == True:
            raise SLLException()

        # remove from the front
        else:
            self.head.next = self.head.next.next

        return

    def remove_back(self) -> None:
        """
        Removes last node in the linked list.
        """

        # if the list is empty remove 1
        if self.is_empty() == True:
            raise SLLException()

        # if the list is 1 set front sentinel to tail sentinel
        elif self.length() == 1:
            self.head.next = self.tail

        # call helper function to remove tail
        else:
            self.remove_back_helper(self.head.next)

        return

    def remove_at_index(self, index: int) -> None:
        """
        removes data at the desired index
        """

        # if the list is empty or index is out of bounds then raise flag
        if self.is_empty() == True or index < 0 or index > self.length() - 1:
            raise SLLException()

        # remove from front if the index is 0
        elif index == 0:
            self.remove_front()

        # call remove_at_index_helper to remove the node at the desired index recursively
        else:
            slot = 0
            self.remove_at_index_helper(slot,index,self.head.next)

        return

    def get_front(self) -> object:
        """
        Pulls data from the first node
        """

        # raise exception if list is empty
        if self.is_empty() == True:
            raise SLLException()

        # return the value if the list is empty
        else:
            return self.head.next.value

    def get_back(self) -> object:
        """
        Pulls data from the last node
        """

        # if list is empty raise exception, if list is one node call get front, if not call get_back_helper
        if self.is_empty() == True:
            raise SLLException()
        elif self.length() == 1:
            return self.get_front()
        else:
            back_value = self.get_back_helper(self.head.next)
            return back_value

    def remove(self, value: object) -> bool:
        """
        The remove method removes the first node that contains the value and returns true, else returns false
        """

        if self.head.next.value == value:
            self.remove_front()
            return True
        else:
            return self.remove_helper(value,self.head.next)


    def count(self, value: object) -> int:
        """
        The method counts the number of nodes that contains the value passed to the method
        """

        # set count to 0
        count = 0

        # return the count of the items
        return self.count_helper(count,value,self.head.next)


    def slice(self, start_index: int, size: int) -> object:
        """
        The method will create a new SLL object that is returned to the user and based on the slice index and size
        passed by the user
        """

        # create a counter that tracks the node slot and create a new linked list
        node_tracker = 0
        new_sll = LinkedList()

        # if index is out of bounds or the size is two big, then raise exception
        if start_index < 0 or start_index >= self.length() or self.length() - size < start_index or size < 0 or self.is_empty() == True:
            raise SLLException()

        # call recursive helper function to help with slicing
        else:
            self.slice_helper(node_tracker, start_index, size, new_sll.head, new_sll.tail, self.head.next)

        # return new_sll
        return new_sll

if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # list = LinkedList()
    # print(list)
    # list.add_front('A')
    # list.add_front('B')
    # list.add_front('C')
    # print(list)
    #
    #
    # print('\n# add_back example 1')
    # list = LinkedList()
    # print(list)
    # list.add_back('A')
    # list.add_back('B')
    # list.add_back('C')
    # print(list)
    #
    #
    # print('\n# insert_at_index example 1')
    # list = LinkedList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #      print('Insert of', value, 'at', index, ': ', end='')
    #      try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #      except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_front example 1')
    # list = LinkedList([1, 2])
    # print(list)
    # for i in range(3):
    #    try:
    #        list.remove_front()
    #        print('Successful removal', list)
    #    except Exception as e:
    #        print(type(e))
    #
    #
    # print('\n# remove_back example 1')
    # list = LinkedList()
    # try:
    #     list.remove_back()
    # except Exception as e:
    #     print(type(e))
    # list.add_front('Z')
    # list.remove_back()
    # print(list)
    # list.add_front('Y')
    # list.add_back('Z')
    # list.add_front('X')
    # print(list)
    # list.remove_back()
    # print(list)
    #
    #
    # print('\n# remove_at_index example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6])
    # print(list)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         list.remove_at_index(index)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # print(list)
    #
    #
    # print('\n# get_front example 1')
    # list = LinkedList(['A', 'B'])
    # print(list.get_front())
    # print(list.get_front())
    # list.remove_front()
    # print(list.get_front())
    # list.remove_back()
    # try:
    #     print(list.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    #
    # print('\n# get_back example 1')
    # lst = LinkedList([1, 2, 3])
    # lst.add_back(4)
    # print(lst.get_back())
    # lst.remove_back()
    # print(lst)
    # print(lst.get_back())
    # lst.remove_back()
    # lst.remove_back()
    # lst.remove_back()
    # try:
    #     print(lst.get_back())
    # except Exception as e:
    #     print(type(e))
    #
    #
    # print('\n# remove example 1')
    # list = LinkedList(["first", "second", "third", "fourth"])
    # print(list)
    # for value in ["first"]:
    #   print(list.remove(value), list.length(), list)
    #
    #
    # print('\n# count example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    #
    #
    # print('\n# slice example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = list.slice(1, 3)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")
    #
    #
    # print('\n# slice example 2')
    # list = LinkedList([])
    # print("SOURCE:", list)
    # slices = [(0, 0), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", list.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")

