# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 2
# Description: The dynamic array portion of the project creates a dynamic array ATD to be used in the implementation of
#              other ATDs, bag, queue, stack, and max stack.

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def incerment_size(self):
        """
        increment size by one
        """

        self.size += 1

    def decrement_size(self):
        """
        decrement size by one
        """

        self.size -= 1

    def set_capacity(self, value):
        """
        set new capacity
        """

        self.capacity = value

    def get_capacity(self):
        """
        return the current capacity
        """

        return self.capacity

    def resize(self, new_capacity: int) -> None:
        """
        Resize will create a temp dynamic array with the new_capacity and move all elements from the self dynamic array
        into the temp dynamic array. Once the temp array is populated, the self array is reconstructed with the temp
        dynamic array data at the new_capacity and the temp dynamic array is dereferenced.
        """

        # resize the array if new_capacity is greater than 0 and greater than size
        if new_capacity > 0 and new_capacity >= self.length():

            # create a temp array of new capacity to copy data over
            tempArray = StaticArray(new_capacity)

            # populate new array with data from self array
            for x in range(0, self.length()):
                tempArray.set(x, self.get_at_index(x))

            # set self array to temp array and set the new capacity threshold
            self.data = tempArray
            self.capacity = new_capacity

        return

    def append(self, value: object) -> None:
        """
        Append takes the value that is passed into the method and appends to the end of the array. If the array is full,
        then it is resized at double the capacity
        """

        # populate the data at the end of array if there is room
        if self.length() < self.capacity:

            self.data[self.length()] = value
            self.incerment_size()

        # if there is no room, then resize the array and populate the value at the end of the array
        elif self.length() == self.capacity:
            self.resize(self.capacity * 2)
            self.data[self.length()] = value
            self.incerment_size()

        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method inserts an object at a certain index. It there is room in the array, it will insert it at the
        specific index and shift data over if needed. If there is no room in array, then resize is called to double
        the size of the array
        """

        # raise exception if index is invalid
        if index > self.length() or index < 0:
            raise DynamicArrayException()

        # if the index is current size, then use append
        if index == self.length() and self.length() < self.get_capacity():
            self.append(value)

        # if the index is is less than size then we shift data over to the right and insert the new data at the index
        elif self.length() < self.get_capacity():
            for x in range(self.length(), index, -1):
                self.data[x] = self.get_at_index(x - 1)
            self.set_at_index(index, value)
            self.incerment_size()

        # if the there is no room, then resize the array and insert at the index
        elif self.length() == self.get_capacity():
            self.resize(self.get_capacity() * 2)
            for x in range(self.length(), index, -1):
                self.data[x] = self.get_at_index(x - 1)
            self.incerment_size()
            self.set_at_index(index, value)

        return

    def remove_at_index(self, index: int) -> None:
        """
        The remove_at_index removes an element at a specific index, as long as the index is valid. If the index is not
        the less index, then every element is sifted left until the index. If length is less than 1/4 capacity and
        capacity is greater than 10, reduce capacity by twice the current length. Once reduced, continue with the
        removal.
        """

        # raise exception if index is invalid
        if index >= self.length() or index < 0:
            raise DynamicArrayException()

        # if current size is less than 1/4 capacity but capacity is less than or equal to 10 then do nothing
        if self.length() < (self.get_capacity() / 4) and self.get_capacity() <= 10:
            pass
        # else if size is less than 1/4 capacity either set it to 2 times size if it is greater than 10 or set it to 10
        elif self.length() < (self.get_capacity() / 4):
            if self.length() * 2 > 10:
                self.resize(self.length() * 2)
            else:
                self.resize(10)

        # remove index if it is valid
        if index >= 0 and index < self.length():

            # if it is the last index, set it to none and decrement size
            if index == self.length() - 1:
                self.set_at_index(self.length() - 1, None)
                self.decrement_size()

            # if it is not the last element, shift everything left until index and make length - 1 None
            else:
                for x in range(index, self.length() - 1):
                    self.data[x] = self.data[x + 1]
                self.set_at_index(self.length() - 1, None)
                self.decrement_size()

        return

    def slice(self, start_index: int, size: int) -> object:
        """
        The slice method creates a new DynamicArray that contains elements from current DynamicArray based on the index
        and size that is passed. For example (0,3) would mean pull 3 elements from self DynamicArray starting at index
        0 and storing it in the new DynamicArray. If the start_index and size are out or range or invalid, raise an
        exception.
        """

        # raise exception if start_index and size are out of range or invalid
        if start_index < 0 or start_index >= self.length() or start_index + size > self.length() \
                or size < 0:
            raise DynamicArrayException()

        # if start_index and size are valid and in range begin slicing
        if start_index >= 0 and start_index < self.length() and start_index + size <= self.length() \
                and size >= 0:

            # crate new DynamicArray
            sliceArray = DynamicArray()

            # copy over data from self array to new array
            for x in range(0, size):
                sliceArray.append(self.get_at_index(start_index))
                start_index += 1

            # return new array
            return sliceArray

        return

    def merge(self, second_da: object) -> None:
        """
        This takes a DynamicArray parameter and merges it with with current DynamicArray.
        """

        # append everything from second_da into self array
        for x in range(0, second_da.length()):
            self.append(second_da.get_at_index(x))

        return

    def map(self, map_func) -> object:
        """
        The map method creates a new DynamicArray to return. The new array is populated with data from the old array
        with the data from the old array passed into map_fuc. It works similar to the Python map function.
        """

        # create a blank dynamic array to store the new data
        OutputArray = DynamicArray()

        # iterate through self array to populate the output array using the passed function
        for x in range(0, self.length()):
            OutputArray.append(map_func(self.get_at_index(x)))

        # return array
        return OutputArray

    def filter(self, filter_func) -> object:
        """
        TODO: Write this implementation
        """

        # create a blank dynamic array to store the new data
        OutputArray = DynamicArray()

        # iterate through self array to find when the filter is True and then populate that in output array
        for x in range(0, self.length()):
            if filter_func(self.get_at_index(x)) == True:
                OutputArray.append(self.get_at_index(x))

        # return array
        return OutputArray

        pass

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        The reduce function works like the built-in python function reduce(). It takes a initializer, which will be the
        first value in the sequence and the passed function. If no initializer is passed, then the first element of the
        array is the initializer. Every element after the initializer is changed by the function passed in reduce_func
        and a running total of initializer + all new elements is passed back. If the array is empty, then the
        initializer of none is returned.
        """

        # run reduc_func only if the array has elementes
        if self.is_empty() == False:

            # If the initializer was not passed then the initializer is the first element of the array. Once assigned
            # the reduce_func is applied to the remaining elements of the array and a running total is tracked and
            # returned
            if initializer == None:
                value = self.get_at_index(0)
                for x in range(1, self.length()):
                    value = reduce_func(value, self.get_at_index(x))
                return value

            # If an initializer was passed, then set value to initializer and perform the same calculations
            else:
                value = initializer
                for x in range(0, self.length()):
                    value = reduce_func(value, self.get_at_index(x))
                return value

        # return initializer if the array is empty
        return initializer


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(948)
    print(da)
    da.resize(8)
    print(da)

    print("\n# resize - example 3")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    (da.insert_at_index(0, 200))
    (da.insert_at_index(0, 300))
    (da.insert_at_index(0, 400))
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
