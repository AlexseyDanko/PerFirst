a = int(input("Введите число от 1 до 100:"))
b = int(input("Введите число от 1 до 100:"))
c = int(input("Введите число от 1 до 100:"))
if a<=0 or b<=0 or c<=0:
    print("Помешай кисель , пригорает:")
elif a==b==c:
    print("Треугольник равносторонний")
elif a==c!=b or b==c!=a or a==b!=c:
    print("Треугольник равнобедренный")
elif a!=b!=c:
    print("Треугольник разносторонний")



