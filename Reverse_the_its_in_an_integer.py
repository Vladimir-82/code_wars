def reverse_bits(n):
    '''
    Write a function that reverses the bits in an integer.

    For example, the number 417 is 110100001 in binary.
    Reversing the binary is 100001011 which is 267
    You can assume that the number is not negative.

    '''
    if n == 0:
        return 0
    else:

        result = []
        while n != 1:
            n, s = divmod(n, 2)
            result.append(str(s))
        result.append(str(n))
        lst_exit = []
        step = len(result) - 1
        for i in result:
            lst_exit.append(int(i) * 2 ** step)
            step -= 1
        return sum(lst_exit)


print(reverse_bits(0))
