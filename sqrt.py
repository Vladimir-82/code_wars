def is_square(n):
    # return False if n < 0 or len(str(float(n))) < len(str(float(n**0.5))) else True
    return True if n >= 0 and n**0.5 % 1 == 0 else False
print(is_square(5))