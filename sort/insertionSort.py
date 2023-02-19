def insertionSort(arr):

    for i in range(1, len(arr)):
        
        key = arr[i]
        
        j = i - 1

        while j>= 0 and arr[j] > key:

            arr[j + 1] = arr[j]
            arr[j] = key

            j -= 1

    return arr

array = [5, 2, 12, 12, 1]



def insertSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j= i-1

        print(i, j, key)

        while j >= 0 and arr[j] > key:

            arr[j+1] = arr[j]
            arr[j] = key

            j -= 1

            print(j, key, arr)
    
    return arr



print(insertSort(array))