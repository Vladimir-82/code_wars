def binary_array_to_number(arr):
    '''
    Учитывая массив единиц и нулей, преобразуйте эквивалентное двоичное значение в целое число.
    Однако массивы могут иметь разную длину, а не только 4.
    Testing: [0, 0, 0, 1] ==> 1
    Testing: [0, 0, 1, 0] ==> 2
    Testing: [0, 1, 0, 1] ==> 5
    Testing: [1, 0, 0, 1] ==> 9
    Testing: [0, 0, 1, 0] ==> 2
    Testing: [0, 1, 1, 0] ==> 6
    Testing: [1, 1, 1, 1] ==> 15
    Testing: [1, 0, 1, 1] ==> 11
    '''
    # lst_exit = []
    # lst = [str(i) for i in arr]
    # step = len(lst) - 1
    # for i in lst:
    #     lst_exit.append(int(i) * 2 ** step)
    #     step -= 1
    # return sum(lst_exit)

    return int(''.join(str(i) for i in arr), 2)



arr = [1, 1, 1, 0]
print(binary_array_to_number(arr))