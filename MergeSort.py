def MergeSort(array, indexL, indexR):
    if indexL >= indexR:
        return

    mid = (indexL + indexR)//2
    MergeSort(array, indexL, mid)
    MergeSort(array, mid + 1, indexR)
    merge(array, indexL, indexR, mid)

def merge(array, indexL, indexR, mid):
    #copies created for the arrays
    L_copy = array[indexL:mid + 1]
    R_copy = array[mid+1:indexR+1]

    #checks our position in the array
    L_copy_index = 0
    R_copy_index = 0
    sorted_index = indexL
    
    #while loop can work instead of for
    # it will go through all the copies until there are none
    #elements present within the given array
    while L_copy_index < len(L_copy) and R_copy_index < len(R_copy):
        
    #Lcopy checks if it has a small element, which decides where it will
    #it be placed in a sorted array
        if L_copy[L_copy_index] <= R_copy[R_copy_index]:
            array[sorted_index] = L_copy[L_copy_index]
            L_copy_index = L_copy_index + 1
    
        else:
            array[sorted_index] = R_copy[R_copy_index]
            R_copy_index = R_copy_index + 1
            
    #moves ahead by 1
        sorted_index = sorted_index + 1
    #L and R copy will be be incharge of adding the remaining elements
    while L_copy_index < len(L_copy):
        array[sorted_index] = L_copy[L_copy_index]
        L_copy_index = L_copy_index + 1
        sorted_index = sorted_index + 1

    while R_copy_index < len(R_copy):
        array[sorted_index] = R_copy[R_copy_index]
        R_copy_index = R_copy_index + 1
        sorted_index = sorted_index + 1

