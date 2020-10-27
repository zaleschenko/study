import random


def numbers():
    basic_list = []
    for i in range(20):
        basic_list.append(random.randint(0, 1000))
    return basic_list


my_numbers = numbers()
print(my_numbers)


def minimum(my_list):
    minimal = my_list[0]
    for position_in_list in range(len(my_list)):
        if minimal > my_list[position_in_list]:
            minimal = my_list[position_in_list]
    return minimal


print(minimum(my_numbers))
