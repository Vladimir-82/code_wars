def likes(names):
    '''
    Вы, наверное, знаете систему «лайков» по Facebook и другим страницам.
    Люди могут "лайкать" сообщения в блогах, изображения или другие предметы.
    Мы хотим создать текст, который должен отображаться рядом с таким элементом.
    Реализуйте функцию like :: [String] -> String, которая должна принимать входной массив,
    содержащий имена людей, которым нравится элемент. Он должен возвращать отображаемый текст как
    likes([]) # must be "no one likes this"
    likes(["Peter"]) # must be "Peter likes this"
    likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
    likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
    likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

    '''

    if len(names) < 1:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[-1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[-1]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
print(likes(["Jacob", "Alex", "Den", "Hren"]))