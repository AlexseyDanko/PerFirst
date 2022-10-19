a,b,c = map(int,input("Введите трёхзначное число:")) # используется встроенная функция map
if a == 0 or b == 0 or c == 0:
    print("указано недопустимое значение:")
elif a>0 and b>0 and c>0:
    print(a+b+c)
    print(a*b*c)

