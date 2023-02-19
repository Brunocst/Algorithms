def mergeSort(array):

    if len(array) >1:
    
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0

        while i<len(left) and j<len(right):

            if left[i] <= right[j]:
                array[k] = left[i]
                i+=1
            elif left[i] > right[j]:
                array[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
print(myList)
mergeSort(myList)
print(myList)

