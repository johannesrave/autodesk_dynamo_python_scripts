# return masked string
import re

def maskify(cc):
    return re.sub(r'(\w)(\w{1,4})\b', r'#\2', cc)

maskify('55555555555')

str.replace()