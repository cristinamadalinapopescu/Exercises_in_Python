# #Scrieti un algoritm care primeste un cod IBAN de Romania  si il valideaza (intoarce True daca e valid, False daca nu).
# iban_nev = input('ibanul este: ')
# lungimea_iban = len(iban_nev)
# country = iban_nev[:2]
# if iban_nev[:2] == 'RO'and lungimea_iban == 24:
#     print('Iban valid')
# else:
#     print('Iban invalid')

'''Fiind dat un cos cu o lista de cantitati,
si o lista de preturi, sa se afiseze valoarea totala a cosului.'''
# cos_cu_chestii = {'iaurt': 2, 'rahat': 5, 'halva': 7}
# cos_cu_chestii.values()
# suma = sum(cos_cu_chestii.values())
# print(suma)

# Sa se scrie un algoritm care calculeaza factorialul unui numar dat (n! = 1234...*n).
# import math
# a = 5
# math.factorial(a)
# print(math.factorial(a))

# Fiind data o lista cu numere, sa se genereze lista cu cuburile acestora.
# lista_numere = [2, 3, 4, 6]
# lista_cuburi = []
# for i in lista_numere:
#     lista_cuburi.append(i*i*i)
# print(lista_cuburi)

# Scrieti un algoritm care transforma un string in forma lui L33t. Adica inlocuieste caracterele.

# E/e -> 3

# i/I -> 1

# O/o -> 0

# A/a -> 4

# S/s -> 5

# T/t -> 7

# replacements = (('E','3'),('e','3'), ('i','1'), ('I','1'), ('O','0'), ('o','0'), ('A','4'), ('a', '4'), ('S','5'), ('s','5'), ('T','7'), ('t', '7'))
# my_string = 'Eu sunt Cristina.'
# new_string = my_string
# for old, new in replacements:
#     new_string = new_string.replace(old, new)
# print(new_string)

# Scrieti un algoritm care transforma un titlu in forma lui URL:
# - diacriticele devin variantele lor fara diacritice
# - literele mari devin litere mici
# - spatiile devin minus-uri
# - Eliminam caracterele non-alfanumerice, exceptand _, @, !, $, ;, %

# replacements = ((' ', '-'), ('ș','s'), ('â','a'), ('ț','t'), ('ă','a'), ('î','i'),('#',''),('?',''),('^',''))
# titlu = input('Introduceti titlul : ')
# new_string = titlu
# for old, new in replacements:
#     new_string = new_string.replace(old,new)
# new_string = new_string.lower()
# print(new_string)

'''Fiind data o lista cu numere, sa se afiseze toate valorile de pe pozitii impare.
Cu t-urile acelea s-a aratat cate secunde a luat algoritmului sa rezolve problema.'''
# t1 = time.time()
# initial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 78, 3.1]
# print(initial[1::2])
# t2 = time.time()
# print(t2 - t1)

# Conversia unui string de forma "1.234.567,89 Lei" la un float de forma 1234567.89.
# variabila = "1.234.567,89 Lei"
# variabila = variabila.replace('.', '').replace(',', '.').replace('Lei', '')
# un_float = float(variabila)
# print(un_float)