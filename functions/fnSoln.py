################################################
######## Lab XB - Function Defenitions #########
######## Name :                        #########
######## Section:                      #########
################################################

import math

################################################
########      Function 1 : OUTPUT     #########
################################################

def PrintOutput(s):
    print("OUTPUT " + str(s))

################################################
########    Function 2 : Area Calc     #########
################################################

def TriangleArea(a, b):
    PrintOutput(a/2 * b)

################################################
########  Function 3 : Feet to Meters  #########
################################################

def FeetToMeters(f):
    PrintOutput(f * 0.3048)

################################################
########   Function 4 : Polar Coords   #########
################################################

def PolarCoords(x, y):
    PrintOutput("r: " + str(math.sqrt(x**2 + y**2)) +
                ", theta: " + str(round(math.atan2(y, x) * 57.2958, 1)) + " degrees")

################################################
########     Function 5 : LIST SORT    #########
################################################


def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort

def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def ListSort(l):
    n = len(l)
    quickSort(l, 0, n-1)
    PrintOutput("The sorted array is: " + ', '.join(map(str, l)))
