def QuickSort(array, p, r):
    if p >= r:
        return
    
    q = partition(array, p, r)
    QuickSort(array, p, r-1)
    QuickSort(array, p+1, r)

def partition(array, p, r):
    pivot = array[p]
    low = p + 1
    high = r

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1 

        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[p], array[high] = array[high], array[p]

    return high

    # while loop: if curval > pivot then do nothing
    # false? move to the left and move on to the onward element
    # we also have to check if the val is also smaller than pivot

