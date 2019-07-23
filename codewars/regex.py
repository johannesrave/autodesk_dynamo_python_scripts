import re

def is_digit(n):
    if re.match(r'\d+', str(n)) and not re.match(r'^\d+', str(n)):
        return True
    else: return False


print(is_digit(5))