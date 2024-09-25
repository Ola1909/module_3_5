def get_multiplied_digits(number):
    str_number = str(number)
    str_number_0 = str_number.replace('0','')
    first = int(str_number_0[0])

    if len(str_number_0) <= 1:
        return first

    else:
        return first * get_multiplied_digits(int(str_number_0[1:]))

result = get_multiplied_digits(40203)
print(result)
