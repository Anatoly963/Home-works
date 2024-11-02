first=int(input('Введите целое число ', ))
second=int(input('Введите целое число ', ))
third=int(input('Введите целое число ', ))
print ()
if first==second and second== third:
    print ('3 совпадения')
elif first == second or second == third or first==third:
    print('2 совпадения')
else:
    print('0 совпадений')