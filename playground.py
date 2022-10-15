def f(array):
    for i in range(len(array)):
        array[i] *= 2
    return array[0]


numbers = [1, 2, 3]
x = f(numbers)
sum = 0
for n in numbers:
    sum += n
print(sum)