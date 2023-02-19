def binarySearch(array, number, low, high):

    if low <= high:

        mid = (len(array)-1)//2

        if array[mid] == number:
            return array[mid]
        elif array[mid] > number:
            return binarySearch(array, number, low, mid-1)
        else:
            return binarySearch(array, number, mid+1, high)

    return 'number not found'


array = [1, 2, 3, 9]
numb = binarySearch(array, 2, 0, len(array)-1)
print(numb)

