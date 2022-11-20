'''Programul de mai jos calculeaza teorema lui Pitagora pentru un triunghi ABC cu ipotenuza c si catetele a si b.'''

from math import sqrt

latura = input('Alege latura pentru care doresti sa fie aplicata teorema: ')
if latura == 'a':
    b = int(input('Introdu lungimea laturii b: '))
    c = int(input('introdu lungimea laturii c: '))
    a = sqrt((c**2) - (b**2))
    print('Lungimea laturii a este urmatoarea: ')
    print(a)

elif latura == 'b':
    a = int(input('Introdu lungimea laturii a: '))
    c = int(input('Introdu lungimea laturii c: '))

    b = sqrt((c**2) - (a**2))

    print('Lungimea laturii b este urmatoarea: ')
    print(b)

elif latura == 'c':
    a = int(input('Introdu lungimea laturii a: '))
    b = int(input('Introdu lungimea laturii b: '))

    c = sqrt((a**2) + (b**2))

    print('Lungimea laturii c este urmatoarea: ')
    print(c)

else:
    print(' Te rog, selecteaza una dintre laturile a, b si c: ')