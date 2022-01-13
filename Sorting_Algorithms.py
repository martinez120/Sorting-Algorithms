from InsertionSort import InsertionSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from datetime import datetime

startTime = datetime.now()

print("Given array: 10, 20, 30, 5, 10, 15, 5, 7, 8, 9, 10")

array = [10, 20, 30, 5, 10, 15, 5, 7, 8, 9, 10]
InsertionSort(array)
print("InsertionSort: " + str(array))
print("Time InsertSort:" + str(datetime.now() - startTime))

array = [10, 20, 30, 5, 10, 15, 5, 7, 8, 9, 10]
MergeSort(array, 0, len(array) -1)
print("MergeSort:" + str(array))
print("Time MergeSort:" + str(datetime.now() - startTime))

array = [10, 20, 30, 5, 10, 15, 5, 7, 8, 9, 10]
QuickSort(array, 0, len(array) - 1)
print("QuickSort:" + str(array))
print("Time QuickSort:" + str(datetime.now() - startTime))

