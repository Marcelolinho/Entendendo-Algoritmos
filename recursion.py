def fat(x):
    if x == 1:
        return 1
    else:
        return x* fat(x-1)
    
print(fat(4))

def cumsum(target):
    if target == 1:
        return 1

    return target + cumsum(target - 1)

print(cumsum(10))

# Exercício 4.1
def soma(array):
    if len(array) < 2:
        return array[0]

    return array[0] + soma(array[1:])

print(soma([10,20,30,40]))

#Exercício 4.2
def count_list(array, count = 1):
    if len(array) == 1:
        return 1
    elif len(array) == 0:
        return 0

    return count + count_list(array[1:], 1)

print(count_list([12, 3, 2, 3, 4, 5]))

#Exercício 4.3