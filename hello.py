from random import choices

def fruit():
    fruits = ["apple","banana", "cherry","grape","mango"]
    return choices(fruits)[0]


print(fruit())

#var = 1
#var = var
