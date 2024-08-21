def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        lower = [i for i in array[1:] if i <= pivo]
        higher = [i for i in array[1:] if i >= pivo]

        return quicksort(lower) + [pivo] + quicksort(higher)
    
print(quicksort([78, 6, 50, 40, 20, 10, 0]))