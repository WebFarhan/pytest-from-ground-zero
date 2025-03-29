from random import choices

def random_fruit():
    fruits = ["apple","banana", "cherry","grape","mango"]
    return choices(fruits)[0]
