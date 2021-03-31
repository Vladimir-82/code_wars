'''
This time no story, no theory. The examples below show you how to write function
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''
def accum(s):
    output = ''
    multy = 1
    for elem in s:
        output += elem * multy + '-'.upper()
        multy += 1
    return output[:-1].title()

print(accum('abcd'))