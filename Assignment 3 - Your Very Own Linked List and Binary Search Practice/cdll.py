# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 3
# Description: This portion of assignment 3 implements the data structure of doubly linked lists for bags and deques


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        This method adds a node to the front of the DLL
        """

        # if the DLL is empty add a node that also points back to the sentinel and vice versa
        if self.is_empty() == True:
            newNode = DLNode(value)
            self.sentinel.next = newNode
            self.sentinel.prev = newNode
            newNode.next = self.sentinel
            newNode.prev = self.sentinel

        # if the DLL is not empty have the new node point to sentinel and the existing front node, while also having
        # the previous front node and sentinel point to the new node
        else:
            newNode = DLNode(value)
            self.sentinel.next.prev = newNode
            newNode.next = self.sentinel.next
            self.sentinel.next = newNode
            newNode.prev = self.sentinel

        return

    def add_back(self, value: object) -> None:
        """
        This method adds a node to the back of the DLL
        """

        # if DLL is empty point to the new node
        if self.is_empty() == True:
            self.add_front(value)

        # if DLL is not empty that insert new node into DLL link list at the back
        else:
            newNode = DLNode(value)
            self.sentinel.prev.next = newNode
            newNode.prev = self.sentinel.prev
            newNode.next = self.sentinel
            self.sentinel.prev = newNode

        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        inserts at the desired index
        """

        # get the length for fast use later on
        dll_length = self.length()

        # if index is out of bounds raise exception
        if index < 0 or index > dll_length:
            raise CDLLException()

        # if index is 0, add to front
        # if index is length, add to back
        # if index is in the middle, insert at desired index
        if index == 0:
            self.add_front(value)
        elif index == dll_length:
            self.add_back(value)
        else:
            cur = self.sentinel.next
            for x in range(0, dll_length):
                if index == x:
                    newNode = DLNode(value)
                    cur.prev.next = newNode
                    newNode.next = cur
                    newNode.prev = cur.prev
                    cur.prev = newNode
                cur = cur.next

        return

    def remove_front(self) -> None:
        """
        removes a node from the front of the DLL
        """

        # raise exception if node is empty
        if self.is_empty() == True:
            raise CDLLException()

        # else remove current node from front
        else:
            self.sentinel.next = self.sentinel.next.next
            self.sentinel.next.prev = self.sentinel

        return

    def remove_back(self) -> None:
        """
        removes node from the back of the DLL
        """

        # if the DLL is empty raise exception
        if self.is_empty() == True:
            raise CDLLException()

        # else remove the current back node
        else:
            self.sentinel.prev = self.sentinel.prev.prev
            self.sentinel.prev.next = self.sentinel

        return

    def remove_at_index(self, index: int) -> None:
        """
        removes the node from the index that is passed into the method
        """

        # if the DLL is empty raise exception
        if self.is_empty() == True:
            raise CDLLException()

        # save length for faster use later
        dll_length = self.length()-1

        # if index is out of bounds then raise flag
        if index < 0 or index > dll_length:
            raise CDLLException()

        # if index is 0 remove from front
        # if index is last of the list, the remove back
        # else remove node from desired index
        if index == 0:
            self.remove_front()
        elif index == dll_length:
            self.remove_back()
        else:
            cur = self.sentinel.next
            for x in range(0, dll_length):
                if x == index:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                cur = cur.next

        return

    def get_front(self) -> object:
        """
        returns the current front node value
        """

        # raise exception if the list is empty
        if self.is_empty() == True:
            raise CDLLException()

        # if not empty then pull the front node value
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        returns the back node value
        """

        # raise exception if the list is empty
        if self.is_empty() == True:
            raise CDLLException()

        # if not empty then pull the last node value
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        removes all nodes that contains the value passed to remove
        """

        # do nothing if list is empty
        if self.is_empty() == True:
            return False

        # set cur to self.sentinel.next
        cur = self.sentinel.next

        # loop through to find first instance of the value and remove plus return true
        while cur != self.sentinel:
            if cur.value == value:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            cur = cur.next

        # return false if while loop ends
        return False

    def count(self, value: object) -> int:
        """
        returns the count of the value that is passed in the method
        """

        # set count to 0 and cur to self.sentinel.next
        count = 0
        cur = self.sentinel.next

        # iterate through the DLL to count the number of instances of value
        while cur != self.sentinel:
            if cur.value == value:
                count+=1
            cur = cur.next

        # return count
        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        This method swaps two nodes in different indexes. This is done by first finding the nodes in O(N) and then
        swapping in O(1)
        """

        # save length of list for for use later and to prevent multiple calls to self.length()
        dll_length = self.length()

        # raise exception flag if out of bounds
        if index1 < 0 or index2 < 0 or index1 >= dll_length or index2 >= dll_length:
            raise CDLLException()

        # if indexes is the same do nothing
        if index1 == index2:
            return

        # if index1 and index2 are 1 position from each other than swap easily with these two (special case)
        if index1 - index2 == -1 or index1 - index2 == 1:

            # set cur to self.sentinel.next and declare node1 and node2
            cur = self.sentinel.next
            node1 = 0
            node2 = 0

            # iterate through the for list until one of the indexes is found and set node1 and node2 to cur and cur.next
            for x in range(0, dll_length):
                if x == index1 or x == index2:
                    node1 = cur
                    node2 = cur.next
                    break
                cur = cur.next

            # swap pointers for the nodes adjacent to node1 and node2
            node1.prev.next = node2
            node1.next = node2.next
            node2.next.prev = node1
            node2.prev = node1.prev

            # connect node1 and node2
            node1.prev = node2
            node2.next = node1

            # return so next step does not begin
            return

        # temp place holders for first index
        index1node = 0
        index1nodeprev = 0
        index1nodenext = 0

        # temp place holders for second index
        index2node = 0
        index2nodeprev = 0
        index2nodenext = 0

        # set cur to self.sentinel
        cur = self.sentinel.next

        # iterate through the DLL until the nodes are found
        for x in range(0, dll_length):

            # save the nodes for index1 and index2 used for swapping
            if x == index1:
                index1node = cur
                index1nodeprev = cur.prev
                index1nodenext = cur.next
            if x == index2:
                index2node = cur
                index2nodeprev = cur.prev
                index2nodenext = cur.next

            # if both nodes are found before loop ends then break
            if index1node != 0 and index2node != 0:
                break

            cur = cur.next

        # swap node 1 into node 2 place
        index2nodenext.prev = index1node
        index1node.next = index2nodenext
        index2nodeprev.next = index1node
        index1node.prev = index2nodeprev

        # swap node 2 into node 1 place
        index1nodenext.prev = index2node
        index2node.next = index1nodenext
        index1nodeprev.next = index2node
        index2node.prev = index1nodeprev

        return

    def reverse(self) -> None:
        """
        This function reverses a doubly linked list and is done in o(n)
        """

        # if the list is empty or only one node then leave
        if self.is_empty() == True or self.sentinel.next.next == self.sentinel:
            return

        # create a temp know to hold for the swap and
        temp_node = None
        cur = self.sentinel.next
        dll_length = self.length()

        # the for loop goes through DLL and reverses the order of the list
        # it works like taking a list and flipping it upside down and traversing that way
        for x in range(0, dll_length):
            temp_node = cur.prev
            cur.prev = cur.next
            cur.next = temp_node
            cur = cur.prev

        # last is up the sentinel next to temp.prev
        self.sentinel.next = temp_node.prev

        # set cur to sentinel.next
        cur = self.sentinel.next

        # iterate through the reversed links
        for x in range(0,dll_length):
            cur.next.prev = cur
            cur = cur.next

        return

    def sort(self) -> None:
        """
        The method sorts a doubly linked list in o(n^2)
        """

        # return if list is empty or 1 node then do nothing
        if self.is_empty() == True or self.sentinel.next.next == self.sentinel:
            return

        # used to save length so we dont call self.length more than once
        dll_length = self.length()

        # we are using a traditional bubble sort for this
        for x in range(dll_length-1):

            # set cur to self.sentinel.next
            cur = self.sentinel.next

            # inner loop for the bubble sort
            for y in range(dll_length-x-1):

                # if the cur node value is greater than the next node value, then swap
                if cur.value > cur.next.value:
                    node1 = cur
                    node2 = cur.next

                    node1.prev.next = node2
                    node1.next = node2.next
                    node2.next.prev = node1
                    node2.prev = node1.prev

                    node1.prev = node2
                    node2.next = node1

                    # this part is important in order to reset to the correct position and to not jump out of bounds
                    cur = cur.prev

                # set cur to cur.next
                cur = cur.next

        return

    def rotate(self, steps: int) -> None:
        """
        This method rotates DLL to left or right based on the input value from the user (negative:left, positive:right).
        It has a range from -10^9 to 10^9 and is done in o(n)
        """

        # if steps is 0 or list is empty or list is 1 node, then do nothing
        if steps == 0 or self.is_empty() or self.sentinel.next.next == self.sentinel:
            return

        # save length for easy use later and not
        dll_length = self.length()
        shifts = steps % dll_length

        if steps > 0:
            for x in range(0,shifts):
                temp_node = self.sentinel.prev

                # next pointer from node before back node are now pointing to sentinel and vice versa
                self.sentinel.prev.prev.next = self.sentinel
                self.sentinel.prev = self.sentinel.prev.prev

                # insert the black holder holder node as the first node
                self.sentinel.next.prev = temp_node
                temp_node.next = self.sentinel.next
                self.sentinel.next = temp_node
                temp_node.prev = self.sentinel

        elif steps < 0:
            for x in range(0, dll_length-shifts):
                temp_node = self.sentinel.next

                # have sentinel point to sentinel.next.next and vice versa thus dereferncing temp_node
                self.sentinel.next = self.sentinel.next.next
                self.sentinel.next.prev = self.sentinel

                # insert the temp node holder as the back node
                self.sentinel.prev.next = temp_node
                temp_node.prev = self.sentinel.prev
                self.sentinel.prev = temp_node
                temp_node.next = self.sentinel

        return

    def remove_duplicates(self) -> None:
        """
        removes all duplicate nodes from sorted DLL leaving only unique nodes that did not have duplicates. This is done
        in o(n) time.
        """

        # if list is empty or only one node then exist
        if self.is_empty() == True or self.sentinel.next.next == self.sentinel:
            return

        # set cur
        cur = self.sentinel.next

        # for loop to iterate through the DLL and remove duplicates
        for x in range(0, self.length()):

            # if cur node = cur next node and cur next node = cur next next node, then remove cur next node
            if cur.value == cur.next.value and cur.next.value == cur.next.next.value:
                cur.next = cur.next.next
                cur.next.prev = cur
                cur = cur.prev

            # if its just cur node = cur next node, then remove nodes cur and cur next
            elif cur.value == cur.next.value:
                cur.prev.next = cur.next.next
                cur.next.next.prev = cur.prev
                cur = cur.prev

            cur = cur.next

        return

    def odd_even(self) -> None:
        """
        This rearranges the DLL so that all odd index nodes are if the first half of the DLL and all the even index
        nodes are in the second half of the DLL. This is done in o(n) time.
        """

        if self.is_empty() == True or self.sentinel.next.next == self.sentinel or self.sentinel.next.next.next == \
                self.sentinel:
            return

        # save length for easy access later and to not call self.length() multiple times.
        dll_length = self.length()

        # rearrange nodes if there are three nodes
        if dll_length == 3:

            # have variables point to the odd and even node that are being rearranged
            odd_temp = self.sentinel.prev
            even_temp = self.sentinel.next.next

            # have the node after sentinel.next point to odd_temp and vice versa
            self.sentinel.next.next = odd_temp
            odd_temp.prev = self.sentinel.next

            # have the sentinel.prev point to the even_temp and vice versa
            even_temp.next = self.sentinel
            self.sentinel.prev = even_temp

            # connect the odd_temp and event_temp nodes
            odd_temp.next = even_temp
            even_temp.prev = odd_temp

            return

        # rearrange nodes if there are four nodes
        if dll_length == 4:

            # set the odd and even temp placeholders
            odd_temp = self.sentinel.prev.prev
            even_temp = self.sentinel.next.next

            self.sentinel.next.next = odd_temp
            odd_temp.next = even_temp
            even_temp.next = self.sentinel.prev

            self.sentinel.prev.prev = even_temp
            even_temp.prev = odd_temp
            odd_temp.prev = self.sentinel.next

            return

        # -------------------------- this for DLLs that have 5 or more nodes ------------------------------------------

        # first nodes of the chain for odd and even nodes
        odd_nodes = self.sentinel.next
        even_nodes = self.sentinel.next.next

        # keep track of the last node the odd and even block chain
        odd_tail = self.sentinel.next.next.next
        even_tail = self.sentinel.next.next.next.next

        # set cur for iterating through
        cur = self.sentinel.next.next.next.next.next

        # make sure the tail node pointers are attached to the even and odd node chains
        odd_nodes.next = odd_tail
        odd_tail.prev = odd_nodes
        even_nodes.next = even_tail
        even_tail.prev = even_nodes

        # start the while loop at 4
        x = 4

        # while loop that iterates through the length of the list
        while x <= dll_length:

            # placeholder pointers to point to an odd and even node
            odd_temp = None
            even_temp = None

            # assign cur to odd_temp
            if cur != self.sentinel:
                odd_temp = cur

            # assign cur.next to even temp
            if cur.next != self.sentinel:
                even_temp = cur.next

            # update cur after variable pointers are set for odd and even temp
            if cur.next.next != self.sentinel:
                cur = cur.next.next

            # attach the odd_temp to the odd_tail and update odd_tail to odd_temp
            if odd_temp != None:
                odd_tail.next = odd_temp
                odd_temp.prev = odd_tail
                odd_tail = odd_temp

            # attach the even_temp to the even_tail and update even_tail to even_temp
            if even_temp != None:
                even_tail.next = even_temp
                even_temp.prev = even_tail
                even_tail = even_temp

            # increase x by 2 because cur is updated two slots
            x+=2

        # attach even_nodes to odd_tail to complete the chain
        odd_tail.next = even_nodes
        even_nodes.prev = odd_tail

        # sentinel next points to odd nodes and vice versa
        self.sentinel.next = odd_nodes
        odd_nodes.prev = self.sentinel

        # sentinel prev points to even nodes and vice versa
        self.sentinel.prev = even_tail
        even_tail.next = self.sentinel

        # relink prev pointers correctly
        cur = self.sentinel.next
        for x in range(0,dll_length):
            cur.next.prev = cur
            cur = cur.next

        return

    def add_integer(self, num: int) -> None:
        """
        This method will receive another non-negative integer num, add it to the number already stored in the linked
        list, and then store the result of the addition back into the list nodes, one digit per node. This is done in
        O(N + log10K) time. Log10k can be computed with ((num // (10 ** digit_counter)) % 10) where num is the input
        parameter and digit_counter is the position of the digit in the integer starting at position 0.
        """

        # log10k ((1000 // (10 ** 3)) % 10)

        # first, the number of digits of int needs to be recorded and is saved in num_length
        num_length = 1
        num_c = num

        while num_c >= 10:
            num_c = num_c // 10
            num_length += 1

        # set variables that will be used throughout the process
        remainder = 0
        cur = self.sentinel.prev
        dll_length = self.length()

        # if the dll has more digits or same as the int
        if dll_length > num_length:

            # iterate through until all dll_length is reached
            for x in range(0,num_length):

                # get value from node and add the log10k with digit counter and add remainder
                num_temp = cur.value
                num_temp += ((num // (10 ** x)) % 10)
                num_temp += remainder

                # if num_temp is greater than or equal to 10, then sub 10 and remainder 1, else remainder 0
                if num_temp >= 10:
                    num_temp -= 10
                    remainder = 1
                else:
                    remainder = 0

                # update cur.value to num_temp and update cur and digit_counter
                cur.value = num_temp
                cur = cur.prev

            # once the num has been added to the existing nodes, check to see if remainders need to be added.
            while remainder != 0 and cur != self.sentinel:

                # get value and add remainder
                num_temp = cur.value
                num_temp += remainder

                # update num_temp if its 10 or greater and then update remainder
                if num_temp >= 10:
                    num_temp -= 10
                    remainder = 1
                else:
                    remainder = 0

                # update the cur.value and update cur
                cur.value = num_temp
                cur = cur.prev

            # if there is a remainder left and cur is on sentinel node, then add a node with the remainder
            if remainder != 0 and cur == self.sentinel:
                self.add_front(remainder)

        # if the int is more digits than the dll
        else:

            # iterate through until all dll_length is reached
            for x in range(0, num_length):

                # proceed with this if cur is not currently on the sentinel node
                if cur != self.sentinel:

                    # get value from node and add the log10k with digit counter and add remainder
                    num_temp = cur.value
                    num_temp += ((num // (10 ** x)) % 10)
                    num_temp += remainder

                    # if num_temp is greater than or equal to 10, then sub 10 and remainder 1, else remainder 0
                    if num_temp >= 10:
                        num_temp -= 10
                        remainder = 1
                    else:
                        remainder = 0

                    # update cur.value to num_temp and update cur and digit_counter
                    cur.value = num_temp
                    cur = cur.prev

                # else proceed if dll nodes have all be touched
                else:

                    # get the log10k from num and add remainder
                    num_temp = ((num // (10 ** x)) % 10)
                    num_temp += remainder

                    # if num_temp is greater than or equal to 10, then sub 10 and remainder 1, else remainder 0
                    if num_temp >= 10:
                        num_temp -= 10
                        remainder = 1
                    else:
                        remainder = 0

                    # add the num_temp to a new node in the front and update digit_counter
                    self.add_front(num_temp)

            # if a remainder still exists, add a front node with the remainder
            if remainder != 0:
                self.add_front(remainder)

        return

if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_front('A')
    # print(lst)
    # lst.add_front('B')
    # print(lst)
    # lst.add_front('C')
    # print(lst)
    #
    # print('\n# add_back example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_back('C')
    # lst.add_back('B')
    # lst.add_back('A')
    # print(lst)
    #
    # print('\n# insert_at_index example 1')
    # lst = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_front example 1')
    # lst = CircularList([1, 2])
    # print(lst)
    # for i in range(3):
    #     try:
    #         lst.remove_front()
    #         print('Successful removal', lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_back example 1')
    # lst = CircularList()
    # try:
    #     lst.remove_back()
    # except Exception as e:
    #     print(type(e))
    # lst.add_front('Z')
    # lst.remove_back()
    # print(lst)
    # lst.add_front('Y')
    # lst.add_back('Z')
    # lst.add_front('X')
    # print(lst)
    # lst.remove_back()
    # print(lst)
    #
    # print('\n# remove_at_index example 1')
    # lst = CircularList([1, 2, 3, 4, 5, 6])
    # print(lst)
    # for index in [3]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # print(lst)
    #
    # print('\n# get_front example 1')
    # lst = CircularList(['A', 'B'])
    # print(lst.get_front())
    # print(lst.get_front())
    # lst.remove_front()
    # print(lst.get_front())
    # lst.remove_back()
    # try:
    #     print(lst.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    # print('\n# get_back example 1')
    # lst = CircularList([1, 2, 3])
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
    # print('\n# remove example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [7, 3, 3, 3, 3]:
    #     print(lst.remove(value), lst.length(), lst)
    #
    # print('\n# count example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    #
    # print('\n# swap_pairs example 1')
    # lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    # test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
    #               (4, 2), (3, 3), (1, 2), (2, 1))
    #
    # for i, j in test_cases:
    #     print('Swap nodes ', i, j, ' ', end='')
    #     try:
    #         lst.swap_pairs(i, j)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# reverse example 1')
    # test_cases = (
    #    [1, 2, 3, 3, 4, 5],
    #    [1, 2, 3, 4, 5],
    #    ['A', 'B', 'C', 'D']
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     lst.reverse()
    #     print(lst)
    #
    # print('\n# reverse example 2')
    # lst = CircularList()
    # print(lst)
    # lst.reverse()
    # rint(lst)
    # lst.add_back(2)
    # lst.add_back(3)
    # lst.add_front(1)
    # lst.reverse()
    # print(lst)
    #
    # print('\n# reverse example 3')
    #
    #
    # class Student:
    #    def __init__(self, name, age):
    #       self.name, self.age = name, age
    #
    #    def __eq__(self, other):
    #        return self.age == other.age
    #
    #    def __str__(self):
    #         return str(self.name) + ' ' + str(self.age)
    #
    #
    # s1, s2 = Student('John', 20), Student('Andy', 20)
    # lst = CircularList([s1, s2])
    # print(lst)
    # lst.reverse()
    # print(lst)
    # print(s1 == s2)
    #
    # print('\n# reverse example 4')
    # lst = CircularList([1, 'A'])
    # lst.reverse()
    # print(lst)
    #
    # print('\n# sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)]
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print(lst)
    #     lst.sort()
    #     print(lst)
    #
    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     lst = CircularList(source)
    #     lst.rotate(steps)
    #     print(lst, steps)
    #
    # print('\n# rotate example 2')
    # lst = CircularList([10, 20, 30, 40])
    # for j in range(-1, 2, 2):
    #     for _ in range(3):
    #         lst.rotate(j)
    #         print(lst)
    #
    # print('\n# rotate example 3')
    # lst = CircularList()
    # lst.rotate(10)
    # print(lst)
    #
    # print('\n# remove_duplicates example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
    #     [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
    #     [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
    #     list("abccd"),
    #     list("005BCDDEEFI")
    # )
    #
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.remove_duplicates()
    #     print('OUTPUT:', lst)
    #
    # print('\n# odd_even example 1')
    # test_cases = (
    # [1, 2, 3, 4, 5], list('ABCDE'),
    # [], [100], [100, 200], [100, 200, 300],
    # [100, 200, 300, 400],
    # [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    # )
    #
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.odd_even()
    #     print('OUTPUT:', lst)
    #
    # test_cases = (
    #     ([1, 2, 3], 10456), ([], 25),
    #     ([2, 0, 9, 0, 7], 108), ([9, 9, 9], 9_999_999)
    # )
    # for list_content, integer in test_cases:
    #     lst = CircularList(list_content)
    #     print('INPUT :', lst, 'INTEGER', integer)
    #     lst.add_integer(integer)
    #     print('OUTPUT:', lst)
