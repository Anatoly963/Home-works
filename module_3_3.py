def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_dict={'a':15, 'b':'silk', 'c':2}
values_list = [True]
values_list_2 = [54.32, 'Строка' ]

print_params(a=10, b= 30, c=70)                 # программа работает на консоли: 10 30 70
print_params(b=25)                              # программа работает на консоли: 1 25 True
print_params(c=[1, 2, 3])                       # программа работает на консоли: 1 строка [1, 2, 3]
print_params([1, 2])                            # программа работает на консоли:[1, 2] строка True
#print_params(a=5, b= "проб", c=40, d=11)       # Ошибка: got an unexpected keyword argument 'd'
print_params(*values_list, [1, 2, 3])        # программа работает на консоли: True [1, 2, 3] True
print_params(*values_list_2, 42)             # программа работает на консоли: 54.32 Строка 42
print_params(**values_dict)                     # программа работает на консоли: 15 silk 2
