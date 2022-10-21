# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления 
# данных. Входные и выходные данные хранятся в отдельных текстовых 
# файлах.

# Пример: 
# aaaaaaabbbbbbccccccccc => 7a6b9c и 
# 11a3b7c => aaaaaaaaaaabbbccccccc

import os
os.system('cls')

def encode_file(my_text):  
    str_code = ''
    count = 1       
    for i in range(len(my_text)):
        if i < len(my_text)-1:
            if my_text[i] == my_text[i + 1]:
                count += 1
            else:
                str_code += str(count) + my_text[i]
                count = 1
        else:
            str_code += str(count) + my_text[i]
    return str_code



def decode_file(strc):
    count = ''
    result = ''
    for i in strc:
        if i.isdigit():
            count += i
        else:
            result += i * int(count)
            count = ''
    return result

text = input('Введите текст для сжатия: ')
# print(f'Предоставлен следующий текст: \n{text}')
with open('task_4_восстановленный_текст.txt', 'w') as data:
    data.write(text)

with open('task_4_восстановленный_текст.txt', 'r') as data:
    my_text = data.read()

strc = encode_file(my_text)
print(f'Текст после сжатия: \n{strc}') 

with open('task_4_текст_после_сжатия.txt', 'w') as data:
    data.write(strc)

with open('task_4_текст_после_сжатия.txt', 'r') as data:
    my_text = data.read()

total = decode_file(my_text)
print(f'Текст после восстановления: \n{total}') 

with open('task_4_восстановленный_текст.txt', 'w') as data:
    data.write(total)
  