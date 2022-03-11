# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 2
# Description: This portion of the assignment implements a stack data structure. The stack works by pushing the value
#              the top of the stack and only allowing the top value to be removed (LIFO).

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da_val.length()) + " elements. ["
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
        Pushes the past value to the top of the stack. This is done in O(1) because it only needs to store are the
        current top position
        """

        # push to the top of the stack
        self.da_val.append(value)

        return

    def pop(self) -> object:
        """
        The value are the top of the stack is removed. The implementation is O(1) because no searches or loops are
        needed. Only the index number of the top value is needed.
        """

        # raise exception if the stack is empty
        if self.is_empty() == True:
            raise StackException()

        # save the value that is at the top of the stack to return to user
        value = self.da_val.get_at_index(self.size()-1)

        # remove the value at the top of the stack
        self.da_val.remove_at_index(self.size()-1)

        # return the value that is popped
        return value

    def top(self) -> object:
        """
        Returns the current value that is at the top of the stack and does not pop it. It is implemented in O(1) because
        only the last index is needed to determine the value.
        """

        # raise exception if the stack is empty
        if self.is_empty() == True:
            raise StackException()

        # return the current value at the top of the stack
        return self.da_val.get_at_index(self.size()-1)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = Stack()
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
    s = Stack()
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
