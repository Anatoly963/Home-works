numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print()
print('numbers ', numbers)      # печать списка заданного изначально в задаче
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):   # формируем цикл перебора чисел в списке значений
    d = 0                       # формируем флаг простоты числа (вместо is_prime)
    if numbers[i] !=1:          # исключаем единицу из простых чисел
        a = numbers[i]          # выбираем число из списка
        for j in range(1, a):   #  цикл подбора делителей для числа из 1ого цикла
            if a % j == 0:
                d = d+1
        if d == 1:
            primes.append(a)    # формирование списка primes
        else:
            not_primes.append(a)    # формирование списка not_primes
print()
print('primes ', primes)            # печать списка primes
print('not_primes ', not_primes)    # печать списка not_primes
