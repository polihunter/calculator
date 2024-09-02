print('Введите два числа ')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
bim = input('Выберите операцию: (Введите +, -, *, /, //, %): ')
if bim == "+":
    c=a+b
    print(a, "+", b, "=", c)

elif bim == "-":
    c=a-b
    print(a, "-", b, "=", c)

elif bim == "*":
    c=a*b
    print(a, "*", b, "=", c)

elif bim == "/":
    c=a/b
    print(a, "/", b, "=", c)

elif bim == "//":
    c=a//b
    print(a, "//", b, "=", c)

elif bim == "%":
    c=(a*b)/100
    print(a, "%", b, "=", c, "%")
print('Вот ваш ответ')
