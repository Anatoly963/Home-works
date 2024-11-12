

result = []
print()
chis = int(input('Введите число от 3 до 20:  '))    # Ввод любого числа от 3 до 20
for i in range(1, chis//2+1):                       # цикл формирования списка result
    for j in range (2, chis):
        if i < j:
            if chis % (i+j) == 0:
                result.append(i)                    # формирование списка result
                result.append(j)                    # формирование списка result
#print(*result)                                     # печать пароля с пробелами
i=0
while i < len(result):
    print(result[i], end='')                        # печать пароля без пробелов (пары чисел друг за другом)
    i = i + 1







