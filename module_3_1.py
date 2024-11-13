#  ПРОГРАММА ДОМАШНЕГО ЗАДАНИЯ (string и list_to_search задаются вне функций, глобальные параметры)

calls = 0
def count_calls ():
    global calls
    calls = calls+1

def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return (string)

def is_contains (string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        a = string.upper() == list_to_search[i].upper()
        if a == True:
            break
        else:
            a=False
    return (a)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('CyCle', ['recycling', 'cYcliC', 'cYcLe']))

print(string_info('Программа'))
#print(string_info('Записи'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic', 'paRCycle', 'Цикл']))

print (calls)

# ***************************************************************

# ПРОГРАММА ВВОДА ПАРАМЕТРОВ С ПОМОЩЬЮ INPUT (string и list_to_search локальные параметры)

calls = 0
def count_calls ():
    global calls
    calls = calls+1

def string_info():
    count_calls()
    string = input('Введите строку: ')
    string = (len(string), string.upper(), string.lower())
    print(string)

def is_contains ():
    #global a
    count_calls()
    string = input('Введите строку: ')
    list_to_search = input('Введите список через пробел: ').split()
    print(string, list_to_search)
    for i in range(len(list_to_search)):
        a = string.upper() == list_to_search[i].upper()
        if a == True:
            break
        else:
            a=False
    print(a)

string_info()
string_info()
string_info()
string_info()
is_contains()
is_contains()

print (calls)















