def get_count(input_str):
    '''
    Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, u as vowels for this Kata (but not y).
    The input string will only consist of lower case letters and/or spaces.
    Вяртае колькасць (колькасць) галосных у дадзеным радку.
    Мы разгледзім a, e, i, o, u галоснымі для гэтай ката (але не ў).
    Уваходны радок будзе складацца толькі з малых літар і / або прабелаў.
    '''
    num_vowels = sum([1 for i in input_str if i in ['a', 'e', 'i', 'o', 'u']])
    return num_vowels

print(get_count('webkiyooaaa'))


# num_vowels = 0
#     for i in input_str:
#         if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#             num_vowels += 1
#     return num_vowels