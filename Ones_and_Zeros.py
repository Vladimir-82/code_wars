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
    while 1 in arr:

        couter = 0
        if arr[0] == 1 and 1 not in arr[1:]:
            arr = (len(arr) - 1) * [1]
            couter +=1
        elif 0 not in arr:
            arr[-1] = 0
            couter += 1
        elif 0 in arr:
    print(arr)

arr = [1, 0, 0]
print(binary_array_to_number(arr))