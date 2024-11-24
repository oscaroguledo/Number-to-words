from numbers import basicdigits

def parse_tens_and_units(number, digits):
    """
    Converts numbers less than 100 to words.
    """
    if number in digits:
        # Direct match for numbers like '10', '20', etc.
        return digits[number]
    if number == '00':
        # Handle special case of '00'
        return ''
    
    tens = number[0] + '0'  # Extract the tens place (e.g., '20')
    units = number[1]       # Extract the units place (e.g., '3')

    if int(tens)==0:
        return digits[units]
    # Combine tens and units appropriately
    return f"{digits[tens]} {digits[units]}" if units != '0' else digits[tens]


def parse_three_digits(number, digits):
    """
    Converts numbers less than 1000 to words.
    """
    if len(number) == 3:
        hundreds = number[0]
        remainder = number[1:]
        if remainder == '00':
            return f"{digits[hundreds]} hundred"
        return f"{digits[hundreds]} hundred and {parse_tens_and_units(remainder, digits)}"
    elif len(number) == 2:
        return parse_tens_and_units(number, digits)
    else:
        return digits[number]  # Single digit
def split_in_threes_from_end(s):
    # Split the string in reverse order into chunks of 3
    return [s[max(0, i-3):i] for i in range(len(s), 0, -3)][::-1]

def getzerostype(i, lang='en'):
    """
    Return the word representation of the group of zeros based on index.
    
    Args:
    i (int): The index of the group of zeros (1 for thousand, 2 for million, etc.)
    
    Returns:
    str: The word representing the group of zeros.
    """
    if lang == 'en':
        if i == 1:
            return 'thousand'
        if i == 2:
            return 'million'
        if i == 3:
            return 'billion'
        if i == 4:
            return 'trillion'
        if i == 5:
            return 'quadrillion'
        if i == 6:
            return 'quintillion'
        if i == 7:
            return 'sextillion'
        if i == 8:
            return 'septillion'
        if i == 9:
            return 'octillion'
        if i == 10:
            return 'nonillion'
        if i == 11:
            return 'decillion'
        if i == 12:
            return 'undecillion'
        if i == 13:
            return 'duodecillion'
        if i == 14:
            return 'tredecillion'
        if i == 15:
            return 'quattuordecillion'
        if i == 16:
            return 'quindecillion'
        if i == 17:
            return 'sexdecillion'
        if i == 18:
            return 'septendecillion'
        if i == 19:
            return 'octodecillion'
        if i == 20:
            return 'novemdecillion'
        if i == 21:
            return 'vigintillion'
        if i == 22:
            return 'unvigintillion'
        if i == 23:
            return 'duovigintillion'
        if i == 24:
            return 'trevigintillion'
        if i == 25:
            return 'quattuorvigintillion'
        if i == 26:
            return 'quinvigintillion'
        if i == 27:
            return 'sexvigintillion'
        if i == 28:
            return 'septenvigintillion'
        if i == 29:
            return 'octovigintillion'
        if i == 30:
            return 'novemvigintillion'
        if i == 31:
            return 'trigintillion'
        if i == 32:
            return 'untrigintillion'
        if i == 33:
            return 'duotrigintillion'
        if i == 34:
            return 'tretrigintillion'
        if i == 35:
            return 'quattuortrigintillion'
        if i == 36:
            return 'quintrigintillion'
        if i == 37:
            return 'sextrigintillion'
        if i == 38:
            return 'septentrigintillion'
        if i == 39:
            return 'octotrigintillion'
        if i == 40:
            return 'novemtrigintillion'
        if i == 41:
            return 'quadragintillion'
        if i == 42:
            return 'unquadragintillion'
        if i == 43:
            return 'duoquadragintillion'
        if i == 44:
            return 'trequadragintillion'
        if i == 45:
            return 'quattuorquadragintillion'
        if i == 46:
            return 'quinquadragintillion'
        if i == 47:
            return 'sexquadragintillion'
        if i == 48:
            return 'septenquadragintillion'
        if i == 49:
            return 'octoquadragintillion'
        if i == 50:
            return 'novemquadragintillion'
        if i == 51:
            return 'quinquagintillion'
        if i == 52:
            return 'unquinquagintillion'
        if i == 53:
            return 'duoquinquagintillion'
        if i == 54:
            return 'trequinquagintillion'
        if i == 55:
            return 'quattuorquinquagintillion'
        if i == 56:
            return 'quinquinquagintillion'
        if i == 57:
            return 'sexquinquagintillion'
        if i == 58:
            return 'septenquinquagintillion'
        if i == 59:
            return 'octoquinquagintillion'
        if i == 60:
            return 'novemquinquagintillion'
        if i == 61:
            return 'sexagintillion'
        if i == 62:
            return 'unsexagintillion'
        if i == 63:
            return 'duosexagintillion'
        if i == 64:
            return 'tresexagintillion'
        if i == 65:
            return 'quattuorsexagintillion'
        if i == 66:
            return 'quinsexagintillion'
        if i == 67:
            return 'sexsexagintillion'
        if i == 68:
            return 'septensexagintillion'
        if i == 69:
            return 'octosexagintillion'
        if i == 70:
            return 'novemsexagintillion'
        if i == 71:
            return 'septuagintillion'
        if i == 72:
            return 'unseptuagintillion'
        if i == 73:
            return 'duoseptuagintillion'
        if i == 74:
            return 'treseptuagintillion'
        if i == 75:
            return 'quattuorseptuagintillion'
        if i == 76:
            return 'quinseptuagintillion'
        if i == 77:
            return 'sexseptuagintillion'
        if i == 78:
            return 'septenseptuagintillion'
        if i == 79:
            return 'octoseptuagintillion'
        if i == 80:
            return 'novemseptuagintillion'
        if i == 81:
            return 'octogintillion'
        if i == 82:
            return 'unoctogintillion'
        if i == 83:
            return 'duooctogintillion'
        if i == 84:
            return 'treoctogintillion'
        if i == 85:
            return 'quattuoroctogintillion'
        if i == 86:
            return 'quinoctogintillion'
        if i == 87:
            return 'sexoctogintillion'
        if i == 88:
            return 'septenoctogintillion'
        if i == 89:
            return 'octooctogintillion'
        if i == 90:
            return 'novemoctogintillion'
        if i == 91:
            return 'nonagintillion'
        if i == 92:
            return 'unnonagintillion'
        if i == 93:
            return 'duononagintillion'
        if i == 94:
            return 'trenonagintillion'
        if i == 95:
            return 'quattuornonagintillion'
        if i == 96:
            return 'quinnonagintillion'
        if i == 97:
            return 'sexnonagintillion'
        if i == 98:
            return 'septennonagintillion'
        if i == 99:
            return 'octononagintillion'
        if i == 100:
            return 'centillion'
    return None

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
