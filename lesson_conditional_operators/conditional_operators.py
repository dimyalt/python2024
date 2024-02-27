# num1 = int(input())
# num2 = int(input())
# if num1 < num2:
#     print(num1, "меньше чем", num2)
# if num1 > num2:
#     print(num1, "больше чем", num2)
#
# if num1 == num2:
#     print(num1, "равно", num2)
# if num1 != num2:
#     print(num1, "не равно", num2)

# word = input()
# if word == "Python":
#     print("Да")
# else:
#     print("Нет")

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# if last_digit == first_digit:
#     print("ДА")
# else:
#     print("Нет")

# a, b, operation = int(input("Введите число а: ")), int(input("Введите число b: ")), input("Введите операцию: ")
# if operation == "+":
#     print(a + b)
# elif operation == "-":
#     print(a - b)
# elif operation == "*":
#     print(a * b)
# elif operation == "/":
#     if b == 0:
#         print("На ноль делить нельзя!")
#     else:
#         print(a / b)
# else:
#     print("Неверная операция")


# year = int(input())
# four_number = year % 10
# third_number = (year % 100) // 10
# if third_number == 0 and four_number == 0:
#     print("YES")
# else:
#     print("NO")

# cell1_x, cell1_y = int(input()), int(input())
# cell2_x, cell2_y = int(input()), int(input())
# if (cell1_x + cell1_y) % 2 == (cell2_x + cell2_y) % 2:
#     print("YES")
# else:
#     print("NO")

# age, gender = int(input()), input()
# if 10 <= age <= 15 and gender == "f":
#     print("YES")
# else:
#     print("NO")

# number = int(input())
# if number == 1:
#     print("I")
# elif number == 2:
#     print("II")
# elif number == 3:
#     print("III")
# elif number == 4:
#     print("IV")
# elif number == 5:
#     print("V")
# elif number == 6:
#     print("VI")
# elif number == 7:
#     print("VII")
# elif number == 8:
#     print("VIII")
# elif number == 9:
#     print("IX")
# elif number == 10:
#     print("X")
# else:
#     print("ошибка")

# number = int(input())
# if (number % 2 != 0) or (number % 2 == 0 and 6 <= number <= 20):
#     print("YES")
# elif (number % 2 == 0 and 2 <= number <= 5) or (number % 2 == 0 and 20 <= number):
#     print("NO")

# col_start_x, row_start_y = int(input()), int(input())
# col_finish_x, row_finish_y = int(input()), int(input())
# if (col_start_x + row_start_y == col_finish_x + row_finish_y) or (col_start_x - row_start_y == col_finish_x - row_finish_y):
#     print("YES")
# else:
#     print("NO")

# col_start_x, row_start_y = int(input()), int(input())
# col_finish_x, row_finish_y = int(input()), int(input())
# if (((col_start_x - 2 == col_finish_x) or (col_start_x + 2 == col_finish_x))
#         and ((row_start_y - 1 == row_finish_y) or (row_start_y + 1 == row_finish_y))):
#     print("YES")
# elif (((col_start_x - 1 == col_finish_x) or (col_start_x + 1 == col_finish_x))
#         and ((row_start_y - 2 == row_finish_y) or (row_start_y + 2 == row_finish_y))):
#     print("YES")
# else:
#     print("NO")

# col_start_x, row_start_y, col_finish_x, row_finish_y = int(input()), int(input()), int(input()), int(input())
# if ((1 <= col_start_x <= 8) and (1 <= col_finish_x <= 8) and (1 <= row_start_y <= 8) and (1 <= row_finish_y <= 8)) and ((col_start_x == col_finish_x) or row_start_y == row_finish_y):
#     print("YES")
# elif (col_start_x + row_start_y == col_finish_x + row_finish_y) or (col_start_x - row_start_y == col_finish_x - row_finish_y):
#     print("YES")
# else:
#     print("NO")

a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8, 15)
print(a)
print(b)
print(c)

for i in range(1000, 10000):  # перебираем числа от 100 до 999
    if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
        print(i)
#
# num = int(input())
# result = 0
# for i in range(1, num + 1):
#     result *= i
# print(result)


# n = int(input())
# a = 0
# while n != 0:
#     s = n % 10
#     if s % 2 == 0:
#         a += s
#     n //= 10
# print(a)

# n = input()
# s = 0
# while n > 10:
#     if n % 2 == 1:
#     s = n % 10
#     n //= 10
# print(s)


# n = 4
# count = 0
# maximum = 0
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
#             #break
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

numb = int(input())
r = ""
counter3 = 0
counter_last = 0
counter_chetn = 0
summa_bolshe_5 = 0
proizv_bolshe_7 = 1
zero_five_counter = 0
l = numb % 10
while numb != 0:
    digit = numb % 10
    if digit == 3:
        counter3 += 1
    if digit == l:
        counter_last += 1
    if digit % 2 == 0:
        counter_chetn += 1
    if digit > 5:
        summa_bolshe_5 += digit
    if digit > 7:
        proizv_bolshe_7 *= digit
    if proizv_bolshe_7 == 0:
        proizv_bolshe_7 = 1
    if digit == 0 or digit == 5:
        zero_five_counter += 1

    numb //= 10

print(counter3)
print(counter_last)
print(counter_chetn)
print(summa_bolshe_5)
print(proizv_bolshe_7)
print(zero_five_counter)


