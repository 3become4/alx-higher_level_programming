#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    mx = max(list_num)
    for n in list_num:
        if mx > n:
            to_sub += n
    return (mx - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rn.keys())
    num = 0
    last_rom = 0
    list_num = [0]
    for i in roman_string:
        for n in list_keys:
            if n == i:
                if rn.get(i) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rn.get(i)]
                else:
                    list_num.append(rn.get(i))
                last_rom = rn.get(i)
    num += to_subtract(list_num)
    return (num)
