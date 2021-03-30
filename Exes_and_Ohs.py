# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive.
# The string can contain any char.
#Проверьте, есть ли в строке одинаковое количество символов «x» и «o».
# Метод должен возвращать логическое значение и не учитывать регистр.
# Строка может содержать любой символ.
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false
def xo(s):
    if s.count('x') == s.count('o'):
        return True
    elif 'x' not in s and 'o' not in s:
        return True
    else:
        return False

print(xo("zzoo".lower()))