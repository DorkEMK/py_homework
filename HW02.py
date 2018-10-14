# coding: utf-8
'''
Программа спрашивает у пользователя предложение на русском языке,
шифрует его с помощью шифра Цезаря: каждая буква должна быть зашифрована с помощью следующей за ней по алфавиту.
Пробел должен остаться пробелом. 
При этом два последних слова в предложении должны быть переставлены местами.
Зашифрованное предложение с перестановкой должно выводиться на экран.
''' 

# создание словаря ciph
ciph = {chr(a):chr(a+1) for a in range(1040,1071)}
ciph['Е'] = 'Ё'
ciph['Ё'] = 'Ж'
ciph['Я'] = 'А'
ciph.update({i.lower():ciph[i].lower() for i in ciph})

# чтение предложения
s = input('Введите предложение: ')

# создание листа зашифрованных слов
words = s.split()  
words_c = [''.join([ciph.get(c, '') for c in word]) for word in words]      
words_c = [w for w in words_c if w != '']

# перестановка последнего и предпоследнего слов
if len(words_c) > 1:
    words_c[-2], words_c[-1] = words_c[-1], words_c[-2]

# если не учитывать пунктуацию, кроме пробелов
# print(' '.join([w for w in words_c]))

# если сохранять всю пунктуацию

# создание списка знаков препинания
# кодировка предложения: 1 - слово, 0 - знак препинания
if s[0] in ciph.keys():
    s_code = '1'
    punc = []
else:
    s_code = '0'
    punc = [s[0]]
for i in range (1, len(s)):
    if s[i] in ciph.keys() and s[i-1] not in ciph.keys():
        s_code += '1'
    elif s[i] not in ciph.keys():
        s_code += '0'
        punc.append(s[i])

# создание итогового предложения
s_ciph = ''
p, w = 0, 0
for c in s_code:
    if c is '0':
        s_ciph += punc[p]
        p += 1
    else:
        s_ciph += words_c[w]
        w += 1
print(s_ciph)
