# Преобразуйте математическое выражение, указанное ниже, в выражение на языке Python и
# укажите результат его вычисления в поле ввода ответа.

print(((-12 + (6 / 17))) / (((1 + 2) ** 4) - (5 * 8)))

# Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения, которые повторяются в нём более одного раза.
# list_num = input().split(" ")
# result = list()
# for i in range(len(list_num)):
#     list_num[i] = int(list_num[i])
#     if list_num.count(list_num[i]) >= 2:
#         result.append(list_num[i])
# # sorted(result)
# # print(' '.join(result))
# for num in result:
#     print(num, end=" ")

# objects = [1, 2, 1, 2, 3]
# ans = 0
# s = list()
# for i in range(len(objects)):
#     if objects[i] not in s:
#         ans += 1
#         s.append(objects[i])
# print(s)

def closest_mod_5(x):
    result = x
    while result % 5 != 0:
        result += 1
    return result

closest_mod_5(9)