print("Это урок по выводу данных")
print("А", "сейчас", "будет", "пример", "по вводу", "данных\n")

# print("Как тебя зовут?")
# name = input()
# print("Привет!", name)
#
# # Или можно записать вот так
# name = input("Как тебя зовут?")
# print("Привет!", name)
#
# # А вот так можно? - Можно
# print("Привет!", input("Как тебя зовут?\n"))

# sep и end
print("31", "12", "2024", sep="-")
print("31", "12", "2024", end="*")
print(" ", " ", " ", sep="-")

# Целые числа
num1 = 7
num2 = 10
num3 = num1 + num2
print(num3)

a = 3
b = 2
print(a ** b)

a = 15 // (16 % 7)
print("a", a)
b = 34 % a * 5 - 29 % 5 * 2
print("b", b)
print(a + b)

# n = int(input())
# n1 = n * -1
# print("n1", n1)
# x = n1 // 2
# print("x", x)
# print(x * -1)

a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)

dlina = 17
visota = 4
print(dlina * "*")
print((dlina % (dlina - 1) * "*") + ((dlina - 2) * " ") + (dlina // (dlina - 1) * "*"))
print((dlina % (dlina - 1) * "*") + ((dlina - 2) * " ") + (dlina // (dlina - 1) * "*"))
print(dlina * "*")

# a = int(input())
# b = int(input())
# kv_sum = (a + b) ** 2
# sum_kv = a ** 2 + b ** 2
# print("Квадрат суммы", a, "и", b, "равен", kv_sum)
# print("Сумма квадратов", a, "и", b, "равна", sum_kv)

n = 1
str_n = str(n)
print(n + int(str_n + str_n)+ int(str_n + str_n + str_n))