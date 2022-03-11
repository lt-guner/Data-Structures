# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 2
# Description: This portion of the project implements a bag ATD. A bag ATD is similar to bag in the real world. Data can
#              be stored, any element can be removed, and any data can be tracked such as a count function.

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        The add method for a bag takes the passed variable and places it in the bag. This is implemented in O(1)
        because it is just placed at the end of the ATD without a need to insert anywhere else. Order is not needed for
        a bag.
        """

        # append value to bag
        self.da.append(value)

        return

    def remove(self, value: object) -> bool:
        """
        The remove method takes the value that is passed and finds the first instance of the value in the array. This
        is done in O(n) because it iterates only until the index is found and then only shifts everything left from that
        index.
        """

        # iterate until the value is found and remove from back, then return true
        for x in range(0,self.size()):
            if self.da.get_at_index(x) == value:
                self.da.remove_at_index(x)
                return True

        # return false if not found
        return False

    def count(self, value: object) -> int:
        """
        The count method takes the value that is passed and counts how many times the value is in the DynamicArray.
        Since 1 iteration of a for loop is used to view each index, O(n) is applied.
        """

        # set count to 0
        count = 0

        # count each instance of the value that occurred
        for x in range(0,self.size()):
            if self.da.get_at_index(x) == value:
                count+=1

        # count
        return count

    def clear(self) -> None:
        """
        The clear method empties the entire bag. This is done on O(1) because a new empty DynamicArray is applied.
        """

        # set self.da to DynamicArray()
        self.da = DynamicArray()

        return

    def equal(self, second_bag: object) -> bool:
        """
        The equals method determines if two bags are equal. It does this by comparing the sizes if there are equal. If
        they are, then the next step is to use the count function to determine if each element from self bag is also
        the same in second bag. This is done in O(n) because of 1 iteration of a for loop. But since the count function
        also has a o(n), which is within an existing o(n) we have O(n^2) for this method.
        """


        # if sizes are different, return false
        if self.size() != second_bag.size():
            return False

        # if both bags are empty return false or if only one is empty return true
        if self.da.is_empty() == True and second_bag.da.is_empty() == True:
            return True
        elif self.da.is_empty() == True or second_bag.da.is_empty() == True:
            return False

        # use
        for x in range(0, self.size()):
            if self.count(self.da.get_at_index(x)) != second_bag.count(self.da.get_at_index(x)):
                return False

        return True


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag(['Eqm^', 'PpZMI', 'e', 'WXt', 'b', 'nx``NzVdF', 'wpZCls', 'xlLa', 'JZMCP', '_C'])
    bag2 = Bag(['_C', 'PpZMI', 'e', 'WXt', 'b', 'nx``NzVdF', 'wpZCls', 'xlLa', 'JZMCP','Eqm^'])
    bag3 = Bag(['jRilT', 'nx``NzVdF', 'XN', 'PpZMI', 'b', 'Eqm^', 'Z[O', 'wpZCls', 'WXt', '_Ai', 'e', 'xlLa'])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    print("\n# equal example 2")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()
    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")
    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))