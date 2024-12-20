

def  test_function(x):
    print(x**3)

    def  inner_function(a):
        m=a*5
        print("Я в области видимости функции test_function")
        print(m)
    с = inner_function(4)
    return

b= test_function(5)
print(b)
c = inner_function(2)  # Этот вызов не работает, выдает ошибку


