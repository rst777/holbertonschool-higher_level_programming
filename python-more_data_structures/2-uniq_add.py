#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = set()
    for num in my_list:
        unique_elements.add(num)
    return sum(unique_elements)
