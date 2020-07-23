# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    indexM = 0
    while (len(arrA) > 0) & (len(arrB) > 0):
        if arrA[0] <= arrB[0]:
            merged_arr[indexM] = arrA.pop(0)
            
        else:  # arrA[0] > arrB[0]
            merged_arr[indexM] = arrB.pop(0)
        
        indexM += 1

    while len(arrA) > 0:
        merged_arr[indexM] = arrA.pop(0)
        indexM += 1

    while len(arrB) > 0:
        merged_arr[indexM] = arrB.pop(0)
        indexM += 1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr
'''
    # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
    # utilize any extra memory
    # In other words, your implementation should not allocate any additional lists 
    # or data structures; it can only re-use the memory it was given as input
    def merge_in_place(arr, start, mid, end):
        # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
'''
