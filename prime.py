def is_prime(num):
    '''
    Define a function that takes one integer argument and returns logical value true or false
    depending on if the integer is a prime.

    Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that
    has no positive divisors other than 1 and itself.
    Requirements

    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive.
    You may be given negative numbers as well (or 0).
    '''
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    return True if counter == 2 else False
print(is_prime(5099))