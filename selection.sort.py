array = [87, 41, 5, 71, 66, 17, 80, 42, 23, 88, 78, 53, 35, 19, 40]
print("Array original:", array)

for i in range(len(array)):
    min_index = i    
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i]

print("Array ordenado:", array)