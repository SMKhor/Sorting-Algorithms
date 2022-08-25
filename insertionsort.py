def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        print(alist)
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

#To sort an array of size n in ascending order:
#1: Iterate from array[1] to array[n] over the array.
#2: Compare the current element to its predecessor.
#3: If the key element is smaller than its predecessor, compare it to the elements before.
#Move the greater elements one position up to make space for the swapped element.
