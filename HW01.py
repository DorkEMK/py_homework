import sys
# part 1
w1 = input('Enter the word: ').strip(' !?.,')
for i in range(1, len(w1), 2):
    if w1[i] != 'а' and w1[i] != 'к':
        print(w1[i], end = '')
    else:
        continue
print('\n')
# part 2
n = int(input('Enter the number: '))
# todo : check if number is natural
for i in range (0,n):
    w2 = input('Enter the word: ').strip(' !?.,')
    if w2 != 'программирование':
        print(w2)
    else: sys.exit(0)
# part3
w3 = input('Enter the word: ').strip(' !?.,')
print(w3[:len(w3)//2])
print((w3[-len(w3)//2:])[::-1])