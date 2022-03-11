# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 5
# Description: This portion of the project implements a min heap


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        The add method adds a value node to the heap. This runs in O(LogN) complexity because the node being added, may
        need to be moved up if it is less than the parent.
        """

        # if the heap is empty, then just add to beginning and return
        if self.is_empty() == True:
            self.heap.append(node)
            return

        # if heap has a value, then add to heap and save the index
        self.heap.append(node)
        index = self.heap.length() - 1

        # a while is used to check if the parent nodes are greater than the child and if swaps until the nodes are in
        # order or the head is reached
        while index > 0:
            if self.heap.get_at_index((index-1)//2) > self.heap.get_at_index(index):
                parent_temp = self.heap.get_at_index((index-1)//2)
                child_temp = self.heap.get_at_index(index)
                self.heap.set_at_index((index-1)//2,child_temp)
                self.heap.set_at_index(index,parent_temp)
                index = (index-1)//2
            else:
                return

        return

    def get_min(self) -> object:
        """
        This returns the min value of the help and runs in O(1) complexity because it removes the top of the heap
        """

        # raise exception if heap is empty
        if self.is_empty() == True:
            raise MinHeapException()

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        The remove_min method removes the value top of the heap. It runs in O(LogN) because the value from the last
        entry that is placed at the head, needs to percolate back down to the new correct spot.
        """

        # raise exception if heap is empty
        if self.is_empty() == True:
            raise MinHeapException()

        # if the heap has one node, then pop and return the value
        if self.heap.length() == 1:
            min_value = self.heap.pop()
            return min_value

        # save current min value, pop end of heap, and place in head
        min_value = self.heap.get_at_index(0)
        heap_end = self.heap.pop()
        self.heap.set_at_index(0,heap_end)

        # -------- percolate the heap so the order is correct

        # save length ofr later use and set index
        heap_length = self.heap.length()
        index = 0

        # a while loop is used to percolate the values downward until the end of the array is reached
        while index < heap_length:

            # both children exist then percolate by comparing the two children and percolating by the smaller of the two
            if heap_length > (2*index+1) and heap_length > (2*index+2):
                if self.heap.get_at_index((2*index+1)) <= self.heap.get_at_index((2*index+2)):
                    if self.heap.get_at_index(index) > self.heap.get_at_index(2*index+1):
                        parent_temp = self.heap.get_at_index(index)
                        child_temp = self.heap.get_at_index(2*index+1)
                        self.heap.set_at_index(index, child_temp)
                        self.heap.set_at_index(2*index+1, parent_temp)
                    index = 2*index+1
                else:
                    if self.heap.get_at_index(index) > self.heap.get_at_index(2*index+2):
                        parent_temp = self.heap.get_at_index(index)
                        child_temp = self.heap.get_at_index(2*index+2)
                        self.heap.set_at_index(index, child_temp)
                        self.heap.set_at_index(2*index+2, parent_temp)
                    index = 2*index+2

            # if only left child exists, then swap
            elif heap_length > (2*index+1):
                if self.heap.get_at_index(index) > self.heap.get_at_index(2*index+1):
                    parent_temp = self.heap.get_at_index(index)
                    child_temp = self.heap.get_at_index(2 * index + 1)
                    self.heap.set_at_index(index, child_temp)
                    self.heap.set_at_index(2 * index + 1, parent_temp)
                index = 2 * index + 1

            # break if no conditions pass
            else:
                break

        # return min_value
        return min_value

    def build_heap(self, da: DynamicArray) -> None:
        """
        The build_heap method takes a dynamic array and builds a heap. This is done in O(N) time. Two while loops are
        used, however both while loops are passed different arguments and the inner while loop is not dependent on
        the outer while loop. The inner loop always runs the same amount of iterations which is an the middle index
        of the array (meaning constant). The outer loop is not a constant but doesn't have an incrementing or
        decrementing a counter or iterator. It will only continue once final heap analysis has no swaps.
        """

        # starting index is the parent of the last leaf of the heap
        heap_length = da.length()
        index = (heap_length-1) // 2

        # This while loop starts at the middle index which will be last parent node with a child and percolates up
        # by swapping child nodes as needed. Each iterating decrements index by 1 until the heap is built.
        count = 1
        while count != 0:
            count = 0
            index = (heap_length - 1) // 2
            while index >= 0:
                if heap_length > (2*index+1) and heap_length > (2*index+2):
                    if da.get_at_index(2*index+1) <= da.get_at_index(2*index+2):
                        if da.get_at_index(index) > da.get_at_index(2*index+1):
                            parent_temp = da.get_at_index(index)
                            child_temp = da.get_at_index(2*index+1)
                            da.set_at_index(2*index+1, parent_temp)
                            da.set_at_index(index, child_temp)
                            count+=1
                        index-=1
                    else:
                        if da.get_at_index(index) > da.get_at_index(2*index+2):
                            parent_temp = da.get_at_index(index)
                            child_temp = da.get_at_index(2*index+2)
                            da.set_at_index(2*index+2, parent_temp)
                            da.set_at_index(index, child_temp)
                            count+=1
                        index-=1
                elif heap_length > (2*index+1):
                    if da.get_at_index(index) > da.get_at_index(2*index+1):
                        parent_temp = da.get_at_index(index)
                        child_temp = da.get_at_index(2*index+1)
                        da.set_at_index(2*index+1, parent_temp)
                        da.set_at_index(index, child_temp)
                        count+=1
                    index-=1
                else:
                    index-=1

        # create a temp array
        temp_arr = DynamicArray()

        # assign existing values from the dynamic array into the temp array and assign temp array to self
        for x in range(0, heap_length):
            temp_arr.append(da.get_at_index(x))

        self.heap = temp_arr

        return


# BASIC TESTING
if __name__ == '__main__':

    """
    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())
    """

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([-994, -950, -977, -940, -829, -970, -895, -921, -874, -827, -826, -787, -918, -878, -888, -918, -912,
    -842, -850, -674, -789, -593, -824, -701, -707, -595, -784, -441, -797, -576, -818, -873, -893, -884, -761, -797,
    -239, -577, -850, -504, -644, -414, -160, -126, -168, -651, -813, -145, -577, -421, -453, -564, -230, -744, -747,
    -220, -316, -656, -347, -287, -464, -621, -701, -476, -827, -441, -743, -525, -877, -298, -751, -466, -539, -121,
    24, -312, -571, 193, -409, 571, -264, -485, -571, 311, -218, -109, 108, 375, 202, 576, 202, -189, -602, -361, 110,
    295, 355, -225, -385, -118, -261, 125, -358, -98, -370, 364, -73, -46, -367, -63, -445, 416, -16, 176, -249, 52,
    -594, -62, -276, 730, 466, -281, -402, -305, -559, -550, -138, 524, -373, 547, -229, -65, -194, -559, -268, 291,
    -418, 212, -383, 245, -290, -207, 136, 359, 160, -14, -64, 81, 79, 962, 872, 733, 422, 835, 146, 475, 671, 578, 559,
    884, 944, 661, 279, 659, 238, 435, -507, 321, 946, 138, 70, 139, 137, 962, 775, 541, 756, 481, 819, 942, 665, 545,
    254, 615, 256, 264, -242, 542, -138, 987, 543, 930, 390, 769, 360, 513, 452, 461, -81, 722, -51, 563, 526, 482, 675,
    -301, 280, 985, 392, 646, 178, 387, 891, 620, 121, 209, 231, -265, -336, 918, 625, 769, 696, 602, 952, 631, 484,
    836, 810, 669, -156, 903, 869, 856, 232, 774, 130, 172, 804, 965, 946, 714, 553, 656, -46, 777, -288, 805, -243,
    419, -410, 886, 57, 155, 573, 709, 810, 146, -328, 931, 579, 492, 407, -11, 500, 887, 734, 602, 20, 832, 606, 512,
    508, 599, 297, 814, 336, 88, 160, 700, 590, 871, 264, 217, -1, 667, 231, 462, 427, 269, 990, 909, 836, 425, 68,
    390])
    print(h.remove_min())
    print(h)

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([-131, -977, 974, -859, -34, 703, -312, -793, 661, 893, -573, 353])

    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    h.build_heap(da)
    print(h)