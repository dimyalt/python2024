# Список четных
print([i for i in range(1, int(input()) + 1) if i % 2 == 0])

# Сумма двух списков
l = input().split()
m = input().split()
lst_1 = [int(i) for i in l]
lst_2 = [int(i) for i in m]
for i in range(len(l)):
    print(lst_1[i]+lst_2[i], end=' ')

# Сумма чисел
lst_int = [int(i) for i in input().split()]
lst_sum = sum(lst_int)
print(*lst_int, sep="+", end="=")
print(lst_sum)

# Валидный номер
str = input()
flag = False
str_clear = str.replace("-", "")
if str.startswith('7-') and str[5] == '-' and str[9] == '-' or str[3] == '-' and str[7] == '-':
    str_clear = str.replace("-", "")
    flag = True
    if str_clear.isdigit():
        lst_int = [int(i) for i in str_clear]
        if (len(lst_int) == 11 and lst_int[0] == 7) or len(lst_int) == 10:
            flag = False
else:
    flag = True
if flag == False:
    print("YES")
else:
    print("NO")

# Самый длинный
print(max([len(i) for i in input().split()]))

# Молодежный жаргон
print(*[(m[1:] + m[:1] + 'ки') for m in input().split()])
