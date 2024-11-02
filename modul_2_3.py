my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
b=0
a=len(my_list)
while b <= a:
    if my_list[b] > 0:
        print(my_list[b])
        b=b+1
        if b == a:
            break
        continue
    elif my_list[b] == 0:
        b=b+1
        if b == a:
            break
    else:
        break


