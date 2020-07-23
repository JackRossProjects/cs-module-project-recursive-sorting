# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Base case check
    # If last value >= first value, the array isnt sorted
    if end >= start:
        # Use first and last value to generate midpoint
        mid = start + (end - start) // 2
        # If midpoint is the target, success
        if arr[mid] == target:
            return mid
        # if midpoint is greater than target, recurse through vaues on the right side
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - start)
        # If the midpoint is less than the target, recurse though the values on the left side
        else:
            return binary_search(arr, target, mid + start, end)
      else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

