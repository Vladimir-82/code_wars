def narcissistic(value):
    '''
    A Narcissistic Number is a positive number which is the sum of its own digits,
    each raised to the power of the number of digits in a given base. In this Kata,
    we will restrict ourselves to decimal (base 10).
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
    '''
    lst = [str(i) for i in list(str(value))]
    list_extet = sum([int(i) ** len(str(value)) for i in lst])
    return True if value == list_extet else False

print(narcissistic(1938))

