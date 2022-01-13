def InsertionSort(array):
    #Starts from the first element in the array
    for index in range (1, len(array)):
        currentval = array[index]
        currentpos = index
    #When element is being inserted we need to make
    #sure to move the element if it is larger than the one
    #being compared. Once done the element being
    #added will be moved to the right (if true!)
    while currentpos > 0 and  array[currentpos - 1] > currentval:
        array[currentpos] = array[currentpos - 1]
        currentpos = currentpos - 1

    array[currentpos] = currentval
