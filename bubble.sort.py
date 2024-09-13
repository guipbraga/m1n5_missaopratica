def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

numbers = [64, 34, 25, 12, 22, 11, 90, 88, 76, 55, 43, 21, 9, 4, 3]

bubbleSort(numbers)

print("Array ordenado:", numbers)