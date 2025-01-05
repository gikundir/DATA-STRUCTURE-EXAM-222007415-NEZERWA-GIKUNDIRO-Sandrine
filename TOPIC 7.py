def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


print('Insertion Sort to sort the security system\n__________________________________________')
data = [5, 3, 8, 6, 2]
print("Original:", data)
sorted_data = insertion_sort(data)
print("Sorted:", sorted_data)

