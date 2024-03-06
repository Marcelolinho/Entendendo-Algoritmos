def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio  # Return the index directly if the item is found
        elif chute > item:
            alto = meio - 1  # Adjust the upper bound
        else:
            baixo = meio + 1  # Adjust the lower bound
    
    return None  # Return None if the item is not found

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(pesquisa_binaria(my_list, 10))
