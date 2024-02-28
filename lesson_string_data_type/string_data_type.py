# Fстроки
first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')

# Длина строки
s = 'Python rocks!'
print(len(s))

# Четвертый символ
s = 'Python rocks!'
print(s[3])

# со 2 по 5
s = 'Python rocks!'
print(s[1:5])

# без пробелов
s = '    Python rocks!     '
print(s.strip())

# Большие буквы
s = 'Python rocks!'
print(s.upper())

# Замена
s = 'Python rocks!'
print(s.replace("o", "@"))

# каждый 3й
s = 'Python'
result = ''
for i in range(len(s)):
    if i % 3 != 0:
        result += s[i]
print(result)

# каждая 1
s = '123451'
result = ''
for i in range(len(s)):
    number = s[i]
    if s[i] == '1':
        number = 'one'
    result += number
print(result)

s = '123451'
print(s.replace("1", "one"))

# Удали символы
s = "123@1@@34"
print(s.replace("@", ""))

# Второе вхождение
s = 'affective'
flag = False
counter = 0
for i in range(len(s)):
    if s[i] == 'f':
        counter += 1
if counter == 0:
    print('-2')
elif counter == 1:
    print('-1')
elif counter > 1:
    s = s.replace('f', '-', 1)
    print(s.find('f'))

# Переворот
s = "abch12345h"
start_index, start_flag = 0, False
end_index = 0
for i in range(len(s)):
    if s[i] == 'h' and start_flag is False:
        start_index = i + 1
        start_flag = True
    elif s[i] == 'h' and start_flag is True:
        end_index = i
s_new = s[:start_index] + s[start_index:end_index][::-1] + s[end_index:]
print(s_new)