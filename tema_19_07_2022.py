# Fiind dat un numar citit de la tastatura, sa se afiseze jumatatea lui.
# a = int(input("Introduceti o valoare"))
# jumatatea_lui_a = a/2
# print(jumatatea_lui_a)

# Fiind dat un numar citit de la tastatura, sa se afiseze divizibilitatea lui cu 7.
# a = int(input('Valoare:'))
# print(a % 7==0)

# Fiind dat un numar citit de la tastatura, sa se afiseze radicalul lui.
# import math
# a = int(input('valoare a ='))
# print(math.isqrt(a))

'''Fiind data o valoare de imprumut si un numar de luni in cate o variabila,
sa se afiseze rata lunara luand in calcul dobanda 0% si comision 0%.'''
# a = 3000.50
# b= 12
# d = 0
# c = 0
# rata_lunara = ((a/b) + d + c)
# print(rata_lunara)

# Fiind date 3 numere citite de la tastatura, sa se afiseze media lor armonica.
# a = int(input('numarul a =' ))
# b = int(input('numarul b = '))
# c = int(input('numarul c = '))
# media_armonica= (3 * a * b * c )/((b * c) + (a * c) + (a * b))
# print(media_armonica)

'''Fiind date 3 numere a, b, c si 3 ponderi p, q, r sa se afiseze media lor ponderata. 
Valorile variabilelor pot fi hardcoded.'''
# a = 5
# b = 6
# c = 7
# p = 10
# q = 20
# r = 30
# media_ponderata = ((a*p) + (b*q) + (c * r)) / (p + q + r)
# print(media_ponderata)

'''Fiind date 2 numere a, b,
 sa se afiseze solutia x ecuatiei de gradul 1: a * x + b = 0'''
# a = 2
# b = 3
# x = -(b/a)
# complex_ = complex(x)
# print(complex_)

'''Fiind date 3 numere a, b, c, sa se afiseze solutiile x1, x2 ale ecuatiei 
de gradul 2: a * x ** 2 + b * x + c = 0.'''
# import cmath
# a = 2
# b = 3
# c = 4
# d = (b**2) - (4*a*c)
# x1 = (-b-cmath.sqrt(d))/(2*a)
# x2 = (-b+cmath.sqrt(d))/(2*a)
# print('Solutia este {0} si {1}'.format(x1,x2))

#Fiind dat un numar, sa se afiseze 25% din 50% din numarul respectiv.

# a = int(input('Numarul dorit este: '))
# valoare1 = a * 50/100
# valoare2 = valoare1 * 25/100
# print(valoare2)