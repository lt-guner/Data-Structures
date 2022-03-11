# Course: CS261 - Data Structures
# Student Name: Timur Guner
# Assignment: Assignment 1
# Description: The assignment is to test our knowledge of Python by updating implement 14 different functions. This is
#              to help us practice Python for the upcoming assignments.

from static_array import *
import random

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    This function returns the tuple of the min and max values of a one dimensional array
    """

    # the first element of arr are assigned to min_val and max_val and the arr_size is assigned to arr_size
    min_val = arr.get(0)
    max_val = arr.get(0)
    arr_size = arr.size()

    # iterate through the arry to starting starting at index 1 (if array contains index 1) and compare it to the stored
    # val in min_val and max_val. Update min and max if needed.
    for x in range(1,arr_size):
        if arr.get(x) < min_val:
            min_val = arr.get(x)
        elif arr.get(x) > max_val:
            max_val = arr.get(x)

    # return tuple of min and max
    return(min_val,max_val)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    This function creates a new array from StaticArray based on the following conditions
    1) If the number in the original array is divisible by 3, the corresponding element in the new array should be the
    string ‘fizz’.
    2) If the number in the original array is divisible by 5, the corresponding element in the new array should be the
    string ‘buzz’.
    3) If the number in the original array is both a multiple of 3 and a multiple of 5, the corresponding element in the
    new array should be the string ‘fizzbuzz’.
    4) In all other cases, the element in the new array should have the same value as in the original array.
    """

    # create a new array based on the length of original array
    new_arr = StaticArray(arr.size())

    # a for loop that assigns the values based on the docstring conditions
    for x in range(0,arr.size()):
        if arr.get(x) % 3 == 0 and arr.get(x) % 5 == 0:
            new_arr.set(x,"fizzbuzz")
        elif arr.get(x) % 3 == 0:
            new_arr.set(x,"fizz")
        elif arr.get(x) % 5 == 0:
            new_arr.set(x,"buzz")
        else:
            new_arr.set(x,arr.get(x))

    # returns the new array
    return new_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

# fix reverse
def reverse(arr: StaticArray) -> None:
    """
    The function reverses the array that is passed to the function
    """

    # assign starting and ending pointers to use in while loop
    p_start = 0
    p_end = arr.size() - 1

    # a while loop that reverses the array based on starting and ending positions
    while p_start < p_end:
        temp = arr.get(p_start)
        arr.set(p_start,arr.get(p_end))
        arr.set(p_end, temp)
        p_start+=1
        p_end-=1

    return


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    The rotate function shifts array based on the number of steps that is passed as a parameter. If the number is
    positive, then the function will shift the values to the right. If the value is negative, it will shift the values
    to the left.
    """

    arr_len = arr.size()    # assigns the length of arr to arr_len
    shifts = steps % arr_len    # shifts is the module of based on the modulo of steps passed to arr_len
    new_arr = StaticArray(arr_len)  # create a blank StaticArray called new_arr to store the shifted data
    p_forward = 0   # used as an index to move iterate forward
    p_reverse = arr_len - 1 # used as an index to iterate backwards

    # If steps are greater than 0, we shift to the right. The numbers are shifted to the right equal to shifts. If the
    # current pointer (x) + shifts is greater than the number of indexes of arr, then we begin to store the variables
    # in the beginning of new_arr
    if steps > 0:
        for x in range(0,arr_len):
            if arr_len - 1 < x + shifts:
                new_arr.set(p_forward,arr.get(x))
                p_forward+=1
            else:
                new_arr.set(x+shifts,arr.get(x))

    # If steps is less than 0, we shift the array to left. The numbers are shifted to left equal to shifts. If the
    # x - shifts is less than 0, then we start storing numbers at the end of the new_arr
    elif steps < 0:
        shifts = arr_len - shifts
        for x in range(arr_len - 1, -1, -1):
            if x - shifts < 0:
                new_arr.set(p_reverse,arr.get(x))
                p_reverse-=1
            else:
                new_arr.set(x-shifts,arr.get(x))

    # else is used if 0 was passed to steps
    else:
        for x in range(0,arr_len):
            new_arr.set(x,arr.get(x))

    # return new_arr
    return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    A starting and ending variable are passed to sa_range that is used to created a StaticArray that contains all
    consecutive numbers between start and end (inclusive)
    """

    f_num = start   # assign start to _f_num
    arr_len = 0 # assign 0 to arr_len

    # If end - start is greater than or equal to 0, then the length of the array is end - start + 1. Else, the the
    # length is start - end + 1
    if end - start >= 0:
        arr_len = end - start + 1
    else:
        arr_len = start - end + 1

    # create a StaticArray with length arr_len
    new_arr = StaticArray(arr_len)

    # If end - start >= 0, then we start numbers ascending order from start to end. Else, we store it in descending
    # from start to end
    if end - start >= 0:
        for x in range(0,arr_len):
            new_arr.set(x,f_num)
            f_num+=1
    else:
        for x in range(0,arr_len):
            new_arr.set(x,f_num)
            f_num-=1

    # return new_arr
    return new_arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    The function checks if the StaticArray object that is passed is in ascending order, descending order, or not sorted
    at all. If it is sorted in ascending order the function returns 1. The function returns 2 if the array is sorted in
    descending order. Otherwise, the function returns 0.
    """

    # assign length to arr_len and set ascend and descend to default values of 1 and 0
    arr_len = arr.size()
    ascend = 1
    descend = 2

    # the for loop checks if the array is sorted in ascending order and if not, it sets ascend to 0
    for x in range(0,arr_len):
        if x <= arr_len - 2:
            if arr.get(x+1) <= arr.get(x):
                ascend = 0

    # the for loop checks if the array is sorted in descending order and if not, it sets descend to 0
    for x in range(0,arr_len):
        if x <= arr_len - 2:
            if arr.get(x+1) >= arr.get(x):
                descend = 0

    # return 1 if ascend is 1, return 2 if descend is 2, and return 0 if unsorted
    if ascend == 1:
        return ascend
    elif descend == 2:
        return descend
    else:
        return 0


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    The sa_sort is function takes the StaticArray that is passed and sorts it using insertion sort.
    """

    for index in range(1, arr.size()):
        value = arr.get(index)
        pos = index - 1
        while pos >= 0 and arr.get(pos) > value:
            arr.set(pos+1, arr.get(pos))
            pos -= 1
        arr.set(pos+1,value)

    return


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    The function creates a new StaticArray object with deduped items from the StaticArray that is passed
    """

    # set the size of arr to arr_len, the starting of dup_count to arr_len, and the starting position of pos to 0
    arr_len = arr.size()
    dup_count = arr_len
    pos = 0

    # the for loop decreases dup_count by 1 for every duplicate that is in arr
    for x in range(0,arr_len):
        if x <= arr_len - 2:
            if arr.get(x) == arr.get(x+1):
                dup_count -=1

    # create new_arr which is a new StaticArray that has dup_count for number of items
    new_arr = StaticArray(dup_count)
    new_arr.set(pos,arr.get(0))   # set first element of arr to new_arr
    pos+=1  # increase pos by one

    # if the arr_len is at least 2, pull the second element of arr and set it to new_arr's second element if the second
    # element of arr is not equal to the first element
    if arr_len >= 2:
        if arr.get(0) != arr.get(1):
            new_arr.set(pos,arr.get(1))
            pos+=1

    # this section uses a for loop to check each compare each element of arr and assigns all only one of each element
    # from arr to new_arr
    if arr_len >= 2:
        for x in range(1,arr_len):
            if x <= arr_len - 2:
                if arr.get(x+1) != arr.get(x):
                    new_arr.set(pos,arr.get(x+1))
                    pos+=1

    #return new_arr
    return new_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    The count_sort uses the count sort method for sorting large data. It does this by the following:
    1) Create a count_arr (StaticArray) in which each index counts counts its corresponding element in arr. Example:
       arr = [1,1,3], then count_arr = [0,2,1]
    2) Modify count_arr so that count_arr each element at each index stores the sum of the previous counts. This will
       now indicate the position of each element in the output arr. Example: arr = [1,1,3], then count_arr = [0,2,3]
    3) Populate out_arr (StaticArray) by iterating through arr backwards and placing it in our_arr by the positions
       stored in count_arr
    """

    # assign variables
    max = arr.get(0)
    min = arr.get(0)
    arr_len = arr.size()
    out_arr = StaticArray(arr_len)

    # initialize out_array to 0
    for x in range(0,arr_len):
        out_arr.set(x,0)

    # find min and max values stored in arr
    for x in range(1,arr_len):
        if arr.get(x) < min:
            min = arr.get(x)
        if arr.get(x) > max:
            max = arr.get(x)

    # create a count array to store a count of all numbers by index
    count_arr = StaticArray(max - min + 1)
    count_len = count_arr.size()
    for x in range(0,count_len):
        count_arr.set(x,0)

    # count each element of arr in the corresponding position in count_arr (min is 0 index and max is last index)
    for x in range(0,arr_len):
        count_arr.set((arr.get(x)-min),(count_arr.get(arr.get(x)-min)+1))

    # change count to be position of each element in the array
    for x in range(1,count_arr.size()):
        count_arr.set(x, (count_arr.get(x-1)+count_arr.get(x)))

    # Final step in sorting is to populate the out_arr StaticArray by iterating backwards through arr and placing it
    # in the slot of out_arr based on their position identifier in count_arr. Count_arr is decremented by 1
    for x in range(arr_len-1,-1,-1):
        out_arr.set((count_arr.get(arr.get(x)-min)-1),arr.get(x))
        count_arr.set(arr.get(x)-min,count_arr.get(arr.get(x)-min)-1)

    # reverse the array
    reverse(out_arr)

    # return the out_arr
    return out_arr


# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) -> StaticArray:
    """
    The function sa_intersection finds the intersect from three StaticArrays that are passed. It assigns each intersect
    to a new StaticArray called new_arr and returns it
    """

    # 0 is assigned to three indexes that we used to iterate through when finding intersects
    arr1_index = 0
    arr2_index = 0
    arr3_index = 0

    # the size of each array is stored and used as limits in the while loops, while i_count is used to determine the
    # size of new_arr later
    arr1_len = arr1.size()
    arr2_len = arr2.size()
    arr3_len = arr3.size()
    i_count = 0

    # The while loop is used to compare values in each array until all intersects are found. If a value matches in each
    # of the arrays, i_count is incremented and all three indexes are incremented. Otherwise, comparisons are made to
    # determine which index to increment to find the next intersect
    while(arr1_index < arr1_len and arr2_index < arr2_len and arr3_index < arr3_len):
            if arr1.get(arr1_index) == arr2.get(arr2_index) and arr2.get(arr2_index) == arr3.get(arr3_index):
                i_count += 1
                arr1_index+=1
                arr2_index+=1
                arr3_index+=1
            elif arr1.get(arr1_index) < arr2.get(arr2_index):
                arr1_index+=1
            elif arr2.get(arr2_index) < arr3.get(arr3_index):
                arr2_index+=1
            else:
                arr3_index+=1

    # create new_arr based on i_count size
    if i_count >= 1:
        new_arr = StaticArray(i_count)
    else:
        new_arr = StaticArray(1)
        new_arr.set(0,None)

    # set pos to 1 to be used as the index counter for new_arr and reset all StaticArray index counters
    pos = 0
    arr1_index = 0
    arr2_index = 0
    arr3_index = 0

    # The while loop is used to compare values in each array until all intersects are found and stored in new_arr.
    # It works a lot like the while loop above except we are storing data in new_arr
    while (arr1_index < arr1_len and arr2_index < arr2_len and arr3_index < arr3_len):
        if arr1.get(arr1_index) == arr2.get(arr2_index) and arr2.get(arr2_index) == arr3.get(arr3_index):
            new_arr.set(pos,arr1.get(arr1_index))
            arr1_index += 1
            arr2_index += 1
            arr3_index += 1
            pos+=1
        elif arr1.get(arr1_index) < arr2.get(arr2_index):
            arr1_index += 1
        elif arr2.get(arr2_index) < arr3.get(arr3_index):
            arr2_index += 1
        else:
            arr3_index += 1

    # return new_arr
    return new_arr


# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    A StaticArray is passed to sorted_squares and the squares of each element are stored in a new StaticArray. The new
    StaticArray is sorted in ascending order and returned.
    """

    arr_len = arr.size()    # grab the size of the passed array
    new_arr = StaticArray(arr_len)  # create a new StaticArray to store sorted squared elements from arr
    split = 0   # used to split t
    d_break = 0

    for x in range(0,arr_len):
        new_arr.set(x,(arr.get(x) ** 2))

    # find if there is a middle value
    for x in range(0,arr_len):
        if x < arr_len -1:
            if new_arr.get(x) < new_arr.get(x+1):
                split = x
                break

    # if there was a split in the middle, do the following code
    if split < arr_len-1 and split > 0:

        # create two new StaticArrays based split
        split1 = StaticArray(split + 1)
        split2 = StaticArray(arr_len - split - 1)

        # populate split1 with new_arr data until x is greater than split, then fill the rest of new_arr in split2
        for x in range(0,arr_len):
            if x <= split:
                split1.set(x,new_arr.get(x))
            else:
                split2.set(x-split-1,new_arr.get(x))

        # split1 will need to be reversed because it will be in descending order
        reverse(split1)

        # save size of split1 and split2 for comparison and set all iteration indexes to 0
        split1_len = split1.size()
        split2_len = split2.size()
        split1_index = 0
        split2_index = 0
        new_index = 0

        # The while loops through to compare values in split1 and split2. New_arr is repopulated with the smaller value
        # of split1 and split at the current indexes. Indexes for split1 and split2 are incremented based on what which
        # value was populated in new_arr
        while new_index < arr_len:
            if split1_index < split1_len and split2_index < split2_len:
                if split1.get(split1_index) >= split2.get(split2_index):
                    new_arr.set(new_index,split2.get(split2_index))
                    split2_index+=1
                else:
                    new_arr.set(new_index,split1.get(split1_index))
                    split1_index+=1
            else:
                if split1_index < split1_len and split2_index >= split2_len:
                    new_arr.set(new_index, split1.get(split1_index))
                    split1_index += 1
                else:
                    new_arr.set(new_index, split2.get(split2_index))
                    split2_index += 1
            new_index+=1

    # check to see if all elements are in descending order
    for x in range(0, arr_len):
        if x < arr_len - 1:
            if new_arr.get(x) < new_arr.get(x + 1):
                d_break += 1
                break

    # if the order is fully descending, reverse the order
    if d_break == 0:
       reverse(new_arr)

    return new_arr


# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    The function takes two arrays that contain single digit elements and adds the two array together to produce a new
    array. For example, [1,2,3] + [4,5,6] = [5,7,9] and [9,9,9,9] + [9,9,9] = [1,0,9,9,8]
    """

    new_len = 0
    arr1_len = arr1.size()
    arr2_len = arr2.size()

    if arr1_len >= arr2_len:
        new_len = arr1_len
    else:
        new_len = arr2_len

    new_arr = StaticArray(new_len + 1)
    for x in range(0,new_len+1):
        new_arr.set(x,0)

    # set indexes to iterate through arr1 and arr2
    arr1_index = arr1_len - 1
    arr2_index = arr2_len - 1

    # The for loop calculates the sum of the two arrays by each each digit
    for x in range(new_len-1,-1,-1):

        # If both indexes are greater than -1, then add the integers from arr1[arr1_index] and arr2[arr2_index].
        # If the sum of both are greater than 9, then minus 10 from temp before assigning it x+1 slot of new_arr
        # and adding one to x slot of new_arr, else just add temp to x+1 slot of new_arr
        if arr1_index >= 0 and arr2_index >= 0:
            temp = arr1.get(arr1_index)+arr2.get(arr2_index)
            temp += new_arr.get(x+1)
            if temp >= 10:
                temp -= 10
                add = 1
                prev = new_arr.get(x)
                new_arr.set(x+1, temp)
                new_arr.set(x, add+prev)
            else:
                new_arr.set(x+1, temp)
            arr1_index-=1
            arr2_index-=1

        # If only arr1_index is greater than -1, then add arr1[x] with the the value that is in new_arr[x+1].
        # If temp is greater than 0, then minus 10 from temp before assigning it to new_arr[x+1] and then adding 1 to
        # new_arr[x], else just add temp to new_arr[x+1]
        elif arr1_index >= 0 and arr2_index < 0:
            temp = arr1.get(arr1_index)
            temp += new_arr.get(x+1)
            if temp >= 10:
                temp -= 10
                add = 1
                prev = new_arr.get(x)
                new_arr.set(x+1,temp)
                new_arr.set(x,add+prev)
            else:
                new_arr.set(x + 1, temp)
            arr1_index -= 1

        # If only arr2_index is greater than -1, then add arr2[x] with the the value that is in new_arr[x+1].
        # If temp is greater than 0, then minus 10 from temp before assigning it to new_arr[x+1] and then adding 1 to
        # new_arr[x], else just add temp to new_arr[x+1]
        elif arr1_index < 0 and arr2_index >= 0:
            temp = arr2.get(arr2_index)
            temp += new_arr.get(x+1)
            if temp >= 10:
                temp -= 10
                add = 1
                prev = new_arr.get(x)
                new_arr.set(x+1,temp)
                new_arr.set(x,add+prev)
            else:
                new_arr.set(x+1,temp)
            arr2_index -= 1

    # create a new StaticArray to remove the leading 0 by removing 1 index, else create a blank array
    if new_arr.get(0) == 0:
        final_arr = StaticArray(new_len)
        final_index = new_len - 1
    else:
        final_arr = StaticArray(1)
        final_index = 0

    # If there is a leading 0, then assign the new_arr to final_arr. This iterates backwards to populate the data
    if new_arr.get(0) == 0:
        for x in range(new_len-1,-1,-1):
            if final_index >= 0:
                final_arr.set(x,new_arr.get(x+1))
                final_index -= 1

    # return final_arr if there is a leading 0 in new_arr, else return new_arr
    if new_arr.get(0) == 0:
        return final_arr
    else:
        return new_arr


# ------------------- PROBLEM 13 - SPIRAL MATRIX -------------------------


def spiral_matrix(rows: int, cols: int, start: int) -> StaticArray:
    """
    This function takes three inputs; rows, cols, start. it generates a StaticArray of StaticArrays t0 create a 2D
    representation. Based on the number that is passed in start it will populate the array based on the following.
    1) If the number is positive it will populate the 2D StaticArray starting with start at the top right corner and
       populate the other slots in clockwise manner and increment start each slot
    2) If the number is negative it will populate the 2D StaticArray starting with start at the bottom left corner and
       populate the other slots in counter-clockwise manner and decrement start each slot
    """

    # create a matrix StaticArray to store StaticArrays with a size of rows and save the length
    m_arr = StaticArray(rows)
    m_len = m_arr.size()

    # populate m_arr with StaticArrays each with size of cols
    for x in range(0,m_len):
        m_arr.set(x,StaticArray(cols))

    # set val
    val = start

    # populate the m_arr based on criteria one of the docstring
    if val >= 0:

        # setup up some values to establish the current indexes, keep track of populate rows and columns, keep track of
        # how many squares were populated, and what direction to populate the spiral matrix
        cur_row = 0
        cur_column = cols - 1
        row_move = rows
        column_move = cols
        count = 0
        cur_move = "D"

        # the loop will continue until all slots are filled
        while (count < rows*cols):

            # populate the spiral matrix going down
            if cur_move == "D":
                for x in range(0, row_move):
                    if m_arr[cur_row][cur_column] == None:
                        m_arr[cur_row][cur_column] = val
                        cur_row+=1
                        count+=1
                        val+=1
                cur_move = "L"
                cur_column-=1
                cur_row-=1
                column_move -= 1

            # populate the spiral matrix going left
            if cur_move == "L":
                for x in range(0,column_move):
                    if m_arr[cur_row][cur_column] == None:
                        m_arr[cur_row][cur_column] = val
                        cur_column-=1
                        count+=1
                        val+=1
                cur_move = "U"
                cur_column+=1
                cur_row-=1
                row_move-=1

            # populate the spiral matrix going up
            if cur_move == "U":
                for x in range(0,row_move):
                    if m_arr[cur_row][cur_column] == None:
                        m_arr[cur_row][cur_column] = val
                        cur_row-=1
                        count+=1
                        val+=1
                cur_move = "R"
                cur_column+=1
                cur_row+=1
                column_move-=1

            # populate the spiral matrix going right
            if cur_move == "R":
                for x in range(0,column_move):
                    if m_arr[cur_row][cur_column] == None:
                        m_arr[cur_row][cur_column] = val
                        cur_column+=1
                        count+=1
                        val+=1
                cur_move = "D"
                cur_column-=1
                cur_row+=1
                row_move-=1

    # populate the the spiral matrix if val is negative
    elif val < 0:

        # setup up some values to establish the current indexes, keep track of populate rows and columns, keep track of
        # how many squares were populated, and what direction to populate the spiral matrix
        cur_row = rows - 1
        cur_column = 0
        row_move = rows
        column_move = cols
        count = 0
        cur_move = "R"

        # populate the spiral matrix until all slots are full
        while (count < rows*cols):

            # populate the spiral matrix moving right
            if cur_move == "R":
                for x in range(0, column_move):
                    if m_arr[cur_row][cur_column] == None:
                        m_arr[cur_row][cur_column] = val
                        cur_column+=1
                        count+=1
                        val-=1
                cur_move = "U"
                cur_column-=1
                cur_row-=1
                row_move-=1

            # populate the spiral matrix moving up
            if cur_move == "U":
                for x in range(0, row_move):
                    if m_arr[cur_row][cur_column] == None:
                        m_arr[cur_row][cur_column] = val
                        cur_row-=1
                        count+=1
                        val-=1
                cur_move = "L"
                cur_column-=1
                cur_row+=1
                column_move-=1

            # populate the spiral matrix moving left
            if cur_move == "L":
                for x in range(0, column_move):
                    if m_arr[cur_row][cur_column] == None:
                        m_arr[cur_row][cur_column] = val
                        cur_column-=1
                        count+=1
                        val-=1
                cur_move = "D"
                cur_column+=1
                cur_row+=1
                row_move-=1

            # populate the spiral matrix moving down
            if cur_move == "D":
                for x in range(0, row_move):
                    if m_arr[cur_row][cur_column] == None:
                        m_arr[cur_row][cur_column] = val
                        cur_row+=1
                        count+=1
                        val-=1
                cur_move = "R"
                cur_column+=1
                cur_row-=1
                column_move -= 1

    # return the spiral matrix
    return m_arr


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    The transform_string function takes in three strings; source, s1, and s2. It creates a mutated output string
    (output) that is produce by the following conditions:

    1) If the character from the source string is present in s1, it should be replaced by the character at the same
    index in s2.

    2) Otherwise, if the character is:
        a) Uppercase letter -> replace with ' '
        b) Lowercase letter -> replace with '#'
        c) Digit -> replace with '!'
        d) Anything else -> replace with '='
    """

    # create a blank output screen that store the new contents
    output = ""

    # the for loop iterates through the entire source string and determines what to fill in output
    for x in range(0,len(source)):

        # tracker is used as a variable to determine if a string char in s1 was found in source
        tracker = 0

        # iterate through s1 to find if any characters match in source and add the char (same slot) from s2 to output
        for y in range(0,len(s1)):
            if source[x] == s1[y]:
                output += s2[y]
                tracker = 1

        # if there was was no match from s1, then add characters to output based on the conditions in the nested if
        if tracker == 0:
            if source[x].isupper() == True:
                output += " "
            elif source[x].islower() == True:
                output += "#"
            elif source[x].isdigit() == True:
                output += "!"
            else:
                output += "="

    # return output
    return output


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    """
    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))


    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))


    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(min_max(arr))


    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)


    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
        print(rotate(arr, steps), steps)
    print(arr)


    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3**14)
    rotate(arr, -3**15)
    print(f'Finished rotating large array of {array_size} elements')


    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))


    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)


    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randint(-10**7, 10**7) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')


    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)
    """

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')
    """
    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')
    
    
    print('\n# sa_intersection example 1')
    test_cases = (
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))
    

    print('\n# sorted_squares example 1')
    test_cases = (
        [-966132215, -752512347, -479361468, -441453482, -418115521, -287449941, 478753846, 511782610, 916704467, 919050404, 928655118],
        [1, 2, 3, 4, 5], [-5, -4, -3, -2, -1, 0], [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
    
    
    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]), ([0], [0]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))


    print('\n# spiral matrix example 1')
    matrix = spiral_matrix(1, 1, 7)
    print(matrix)
    if matrix: print(matrix[0])
    matrix = spiral_matrix(3, 2, 12)
    if matrix: print(matrix[0], matrix[1], matrix[2])


    print('\n# spiral matrix example 2')

    def print_matrix(matrix: StaticArray) -> None:
        rows, cols = matrix.size(), matrix[0].size()
        for row in range(rows):
            for col in range(cols):
                print('{:4d}'.format(matrix[row][col]), end=' ')
            print()
        print()

    test_cases = ((4, 4, 1), (3, 4, 0), (2, 3, 10), (1, 2, 1), (1, 1, 42),
                  (4, 4, -1), (3, 4, -3), (2, 3, -12), (1, 2, -42))
    for rows, cols, start in test_cases:
        matrix = spiral_matrix(rows, cols, start)
        if matrix: print_matrix(matrix)

    
    print('\n# transform_strings example 1')
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
    """