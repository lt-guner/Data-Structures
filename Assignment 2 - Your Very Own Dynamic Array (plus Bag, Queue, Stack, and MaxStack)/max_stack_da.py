# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 2
# Description: This portion of the assignment deals with the storing data on stack while also keeping track of the
#              maximum value that is on main stack by pushing it to the top of the max stack. These stacks are done in
#              LIFO.

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()
        self.da_max = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.da_val.length()) + " elements. ["
        out += ', '.join([str(self.da_val[i]) for i in range(self.da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        The push method pushes the value that is passed to the top of stack. There is a separate stack to keep track
        of the highest value that was pushed on the main stack. This is done in O(1) because it is nearly instant.
        """

        # append the value to the top of the stock
        self.da_val.append(value)

        # append the value to the top of the max stack if the stack is empty or if it is greater than or equal to the
        # previous value
        if self.da_max.length() == 0:
            self.da_max.append(value)
        elif self.da_max.get_at_index(self.da_max.length()-1) <= value:
            self.da_max.append(value)

        return

    def pop(self) -> object:
        """
        The pop method removes that last element on top of the main stack. This is done in O(1) because no searches are
        need to loop through the stack. The stack that stores the highest value, is also popped if the value that is
        being popped on the main stack matches.
        """

        # raise exception if the stack is empty
        if self.is_empty() == True:
            raise StackException()

        # store the value that is being popped of the top of the stack
        value = self.da_val.get_at_index(self.size()-1)

        # remove the top value
        self.da_val.remove_at_index(self.size()-1)

        # if the popped value matches the current value on max stack, pop the max stack
        if self.da_max.get_at_index(self.da_max.length()-1) == value:
            self.da_max.remove_at_index(self.da_max.length()-1)

        # return the popped value
        return value

    def top(self) -> object:
        """
        Returns the current value that is on the top of the stack. This is done in O(1).
        """

        # if the stack is empty, raise a flag
        if self.is_empty() == True:
            raise StackException()

        # return the top value if the stack is not empty
        return self.da_val.get_at_index(self.size()-1)

    def get_max(self) -> object:
        """
        Returns the value that is at the top of the max stack. This is done in O(1) because no looping or searching is
        needed.
        """

        # raise exception if the stack is empty
        if self.is_empty() == True:
            raise StackException()

        # return the top value of max stack if there if not empty
        return self.da_max.get_at_index(self.da_max.length()-1)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)


    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
