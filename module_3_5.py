
def get_multiplied_digits(number):
    str_number = str(number)
    if str_number[-1] == '0':
        str_number = str_number[:-1]
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print()
print('Результат: ', result)

result = get_multiplied_digits(402030)
print()
print('Результат: ', result)