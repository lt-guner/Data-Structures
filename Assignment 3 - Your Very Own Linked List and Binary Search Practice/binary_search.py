# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: 3
# Description: This portion of the assignment is for binary searching

import random
import time
from static_array import *


# ------------------- PROBLEM 1 - -------------------------------------------


def binary_search(arr: StaticArray, target: int) -> int:
    """
    This function does a binary search on a sorted list whether it is ascending or descending
    """

    # store the first and last indexes
    start = 0
    end = arr.size()-1

    # find the middle index
    mid = (start + end) // 2

    # if the array is in ascending order then proceed
    if arr.get(start) <= arr.get(end):

        # continuously loop through until index is found or start is greater than end
        while start <= end:

            # get the mid index
            mid = (start + end) // 2

            # if the value pulled using mid index matches target, then return index
            if arr.get(mid) == target:
                return mid

            # if target is less than midpoint, then make end mid - 1 to eliminate the current upper half
            elif target < arr[mid]:
                end = mid - 1

            # else make start mid + 1 to eliminate current lower half
            else:
                start = mid + 1

    else:

        # continuously loop through until index is found or start is greater than end
        while start <= end:

            # the midpoint is calculated differently because its in reverse order
            mid = start + (end - start) // 2

            # does the midpoint contain the query value?
            if arr.get(mid) == target:
                return mid

            # if target is than midpoint, then the lower half of the array is eliminated
            elif target < arr[mid]:
                start = mid + 1

            # else we eliminate the upper half
            else:
                end = mid - 1

    return -1


# ------------------- PROBLEM 2 - -------------------------------------------


def binary_search_rotated(arr: StaticArray, target: int) -> int:
    """
    This does a binary search on an ascending ordered StaticArray that is rotated a few positions
    """
    start = 0
    end = arr.size() -1

    return bin_search_recur(arr,target,start,end)

def bin_search_recur(arr: StaticArray, target: int, start: int, end: int) -> int:
    """
    This is a helper recursive function for binary_search_rotated
    """

    # get middle index
    mid = (start + end) // 2

    # proceed if start is less than mid
    if start <= mid:

        # check if mid matches the target
        if arr.get(mid) == target:
            return mid

        # if upper half is sorted, proceed to checks
        elif arr.get(mid) <= arr.get(end):

            # target is in range, then eliminate lower half
            if target >= arr.get(mid) and target <= arr.get(end):
                return bin_search_recur(arr,target,mid+1,end)

            # else eliminate upper half
            return bin_search_recur(arr, target, start, mid - 1)

        # if lower half is sorted, then proceed
        elif arr.get(start) <= arr.get(mid):

            # if target is in range, then eliminate upper half
            if target >= arr.get(start) and target <= arr.get(mid):
                return bin_search_recur(arr,target,start,mid-1)

            # else eliminate lower half
            return bin_search_recur(arr,target,mid+1,end)

    return -1

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":
    pass


    print('\n# problem 1 example 1')
    src = (-10, -1, -1, 0, 5, 7, 9, 11)
    targets = (-1, -10, 11, 0, 8, 1, -100, 100,-10000000000)
    arr = StaticArray(len(src))
    for i, value in enumerate(src):
        arr[i] = value
    print([binary_search(arr, target) for target in targets])
    arr._data.reverse()
    print([binary_search(arr, target) for target in targets])


    print('\n# problem 1 example 2')

    src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    src = sorted(set(src))
    arr = StaticArray(len(src))
    arr._data = src[:]

    # add 20 valid and 20 (likely) invalid targets
    targets = [-10 ** 9, 10 ** 9]
    targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]

    result, total_time = True, 0
    for target in targets:
        total_time -= time.time()
        answer = binary_search(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)

    arr._data.reverse()
    for target in targets:
        total_time -= time.time()
        answer = binary_search(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)

    """
    print('\n# problem 2 example 1')
    test_cases = (
        ((6, 8, 12, 20, 0, 2, 5), 0),
        ((6, 8, 12, 20, 0, 2, 5), -1),
        ((1,), 1),
        ((1,), 0),
    )
    result = []
    for src, target in test_cases:
        arr = StaticArray(len(src))
        for i, value in enumerate(src):
            arr[i] = value
        result.append((binary_search_rotated(arr, target)))
    print(*result)

    
    print('\n# problem 2 example 2')

    src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    src = sorted(set(src))
    arr = StaticArray(len(src))
    arr._data = src[:]

    # add 20 valid and 20 (likely) invalid targets
    targets = [-10 ** 8, 10 ** 8]
    targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]

    result, total_time = True, 0
    for target in targets:
        # rotate arr random number of steps
        pivot = random.randint(0, len(src) - 1)
        arr._data = src[pivot:] + src[:pivot]

        total_time -= time.time()
        answer = binary_search_rotated(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)
    """
