# The python code outputs empty list. What is the problem with the below code? How to fix it?
my_list = [5, 2, 12, 7, 3, 8]
for element in my_list:
    low = []
    if element < 5:
        low.append(element)
print(low)