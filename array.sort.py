array = [46, 30, 11, 83, 74, 98, 20, 32, 10, 79, 27, 37, 18, 49, 5]
print("Array original:", array)
array.sort()
print("Array ordenado em ordem crescente:", array)
array.sort(key=None, reverse=True)
print("Array ordenado em ordem decrescente:", array)

array_strings = ["Gabriel Santos", "15/03/2010", "123.456.789-10", "MG-12.345.678"]
print("Array original:", array_strings)
array_strings.sort()
print("Array ordenado em ordem crescente:", array_strings)
array_strings.sort(key=None, reverse=True)
print("Array ordenado em ordem decrescente:", array_strings)