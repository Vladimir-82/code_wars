'''
Tap code is a way to communicate using a series of taps and pauses for each letter.
In this kata, we will use dots . for the taps and whitespaces for the pauses.

The number of taps needed for each letter matches its coordinates in the following
polybius square (note the c/k position). Then you "tap" the row, a pause, then the column.
Each letter is separated from others with a pause too.

Tap code-это способ общения с помощью серии нажатий и пауз для каждой буквы. В этом ката мы будем
использовать точки . для отводов и пробелов для пауз.

Количество нажатий, необходимых для каждой буквы, соответствует ее координатам в следующем квадрате
полибия (обратите внимание на положение c/k). Затем вы "нажимаете" на строку, паузу, затем на столбец.
Каждая буква отделена от других паузой.
   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
Input:

A lowercase string of a single word (no whitespaces or punctuation, only letters).
Output:

The encoded string as taps and pauses.

text = "dot"
  "D" = (1, 4) = ". ...."
  "O" = (3, 4) = "... ...."
  "T" = (4, 4) = ".... ...."

output: ". .... ... .... .... ...."


"example" -> ". ..... ..... ... . . ... .. ... ..... ... . . ....."
"more"    -> "... .. ... .... .... .. . ....."

'''
def tap_code_translation(text):
    key = [
        ['A',  'B', 'C\K', 'D',  'E'],
        ['F',  'G',  'H',  'I',  'J'],
        ['L',  'M',  'N',  'O',  'P'],
        ['Q',  'R',  'S',  'T',  'U'],
        ['V',  'W',  'X',  'Y',  'Z'],
    ]

    output = []
    for symb in text:
        for string in key:
            for i in string:
                if symb == i:
                    code = key.index(string) + 1, string.index(i) + 1
                    output.append('.' * code[0] + ' ' + '.' * code[1] + ' ')
                if len(i) > 1:
                    if symb in i:
                        code = 1, 3
                        output.append('.' * code[0] + ' ' + '.' * code[1] + ' ')
    return ''.join(output)[:-1]

string = 'ckck'.upper()
print(tap_code_translation(string))