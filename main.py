from numbers import basicdigits
from utils import parse_tens_and_units,parse_three_digits,split_in_threes_from_end,getzerostype


def convert_cardinal_to_word(number, lang='en'):
    """
    Converts cardinal numbers to words, supporting English.
    """
    digits = basicdigits[lang]
    strnum = str(number)
    
    if not strnum.isdigit():
        return number  # Return original input if it's not a number
    
    length = len(strnum)
    if length == 1 or strnum in digits:
        return digits[strnum]
    elif length == 2:
        return parse_tens_and_units(strnum, digits)
    elif length == 3:
        return parse_three_digits(strnum, digits)
    else:
        splitnumber =split_in_threes_from_end(strnum)
        i=1
        j= len(splitnumber)-1
        words = []
        while i < len(splitnumber):
            words.insert(i-1,f'{parse_three_digits(splitnumber[i-1], digits)} {getzerostype(j, lang=lang)} ') 
            j-=1
            i+=1
        words.append(parse_three_digits(splitnumber[i-1], digits))
        return ''.join(words)
            

def convert_ordinal_to_word(number, lang='en'):
    """
    Converts ordinal numbers to words, supporting English.
    """
    digits = basicdigits[lang]
    strnum = convert_cardinal_to_word(number, lang)
    strlist = strnum.split(' ')
    res  = strlist[0:-1]
    if strlist[-1] in digits.keys():
        res.append(digits[strlist[-1]])
    else:
        res.append(strlist[-1]+'th')

    return ' '.join(res)

# Test cases
print(convert_cardinal_to_word('78'))  # seventy eight
print(convert_ordinal_to_word('78'))
print(convert_cardinal_to_word('105'))  # one hundred and five
print(convert_cardinal_to_word('300'))  # three hundred
print(convert_cardinal_to_word('999'))  # nine hundred and ninety-nine
print(convert_cardinal_to_word('20'))  # twenty
print(convert_cardinal_to_word('74890'))  # seven
print(convert_cardinal_to_word('74548967670'))  # seven
print(convert_ordinal_to_word('0'))
