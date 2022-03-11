# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 2
# Description: This portion of assignment implements a queue. When a value is passed to a queue, it is store at the
#              back. Only values at the top of queue can be removed (FIFO)

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da[i]) for i in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        This pushes the value at the end of the queue. This is done in O(1) because no searches or readjustments are
        needed to insert the value
        """

        # append value to top of the queue
        self.da.append(value)

        return

    def dequeue(self) -> object:
        """
        The method dequeue removes the value at the beginning of the queue (index 0) and moves everything over one index
        to the left. The implementation is O(n) because a single iteration is used to move everything one index over.
        """

        # raise exception if the queue is empty
        if self.is_empty() == True:
            raise QueueException

        # store value that is at th
        value = self.da.get_at_index(0)

        # remove index 0 and shift everything one index over
        self.da.remove_at_index(0)

        # return the value that was removed
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)


    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
