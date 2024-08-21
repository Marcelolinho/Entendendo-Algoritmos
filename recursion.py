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