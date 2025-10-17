a , b = map(int, input().split())
if b == 0:
    print('Ничего у тебя не получится')
else:
    num1 = a // b
    num2 = a % b
if num2 == 0:
    print('Нет остатка')
else:
    print('Остаток есть' + num2)
print(num1)