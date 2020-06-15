# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    complete = False

    while not complete:
        swap_made = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_made = True
        if not swap_made:
            complete = True
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=0):
    # Your code here
    counts = [0 for i in range(maximum+1)]

    for i in range(len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[arr[i]] += 1
    
    arr = []

    for i in range(len(counts)):
        if counts[i] > 0:
            arr += [i] * counts[i]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    
    return arr 


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(insertion_sort(arr1))