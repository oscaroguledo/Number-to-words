
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
