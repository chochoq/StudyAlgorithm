array  = [('박복수,88'),('김호랭,44'),('김자빱,23')]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))


print(sorted(array, key=lambda x: x[1]))
