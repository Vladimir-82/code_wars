def compute_sum(n):
    '''
    Find the sum of the digits of all the numbers from 1 to N (both ends included).
    '''
    lst_extit = []
    lst = [str(i) for i in range(1, n + 1)]
    for el in lst:
        lst_extit.extend(list(el))

    return sum([int(el) for el in lst_extit])

print(compute_sum(10))