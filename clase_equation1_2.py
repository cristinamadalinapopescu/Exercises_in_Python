# Sa se scrie clase pentru urmatoarele:
# 1. FirstDegreeEquation, pentru a * x + b = 0
# cu proprietatile a, b, si metoda solutie(), care returneaza x.
# class FirstDegreeEquation:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def solutie(self):
#         x = -self.b / self.a
#         return x
#
#
# la_solutia = FirstDegreeEquation(3, 15)
# la_solutia = FirstDegreeEquation(2, 1)
# print(la_solutia.solutie())

# 2. SecondDegreeEquation, pentru a * x * x + b * x + c
# cu proprietatile a, b, c, si metoda solutii(), care returneaza o
# tupla cu x1 si x2.


import cmath
# import math
#
#
# class SecondDegreeEquation:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def solutii(self):
#         d = (self.b ** 2) - (4 * self.a * self.c)  # discriminantul
#
#         if d < 0:
#             print('Ecuatia este fara solutii reale: ')
#             x1 = (-self.b + cmath.sqrt(d)) / 2 * self.a
#             x2 = (-self.b - cmath.sqrt(d)) / 2 * self.a
#             return x1, x2
#         if d == 0:
#             x = (-self.b + math.sqrt(d) / 2 * self.a)
#             print('Ecuatia are o singura solutie x: ')
#             return x, x
#         else:
#             x1 = (-self.b + math.sqrt(d)) / 2 * self.a
#             x2 = (-self.b - math.sqrt(d)) / 2 * self.a
#             print('Ecuatia are doua solutii reale: ')
#         return x1, x2
#
#
# solutia = SecondDegreeEquation(1, 4, 5)
# print(solutia.solutii())

# 3. OlxAd, cu titlu, descriere, pret, link:

# class OlxAd:
#     def __init__(self, titlu, descriere, pret, link):
#         self.titlu = titlu
#         self.descriere = descriere
#         self.pret = pret
#         self.link = link
#
#     def __str__(self):
#         return f'{self.titlu} {self.descriere} {self.pret} {self.link}'
#
#
# p1_Olx = OlxAd('Masina de spalat rufe', 'Stare:noua', '860 RON', 'https//lulitruli-olx.com')
# p2_OLx = OlxAd('Ghete de iarna', 'marimea: 38', '120 RON', 'https//lala-olx.com')
#
# print(p1_Olx)
# print(p2_OLx)

# 4. Tree, cu proprietatea base pentru bradul desenat in exercitiul anterior.
# b) Sa se afiseze un brad de forma:  #exercitiul acesta trebuie transformat in clasa cu functii

#       #
#      ###
#     #####
#    #######
#   #########
#  ###########

# i = 1
# var = 10
# while i < var:
#     print(' ' * ((var - 1 - i) // 2) + '#' * i)
#     i += 2

# aici am transformat exercitiul de mai sus in clasa cu functii

# class Tree:
#     def __init__(self, base):
#         self.base = base
#
#     def baza(self):
#         i = 1
#         while i < self.base:
#             print(' ' * ((self.base - 1 - i) // 2) + '#' * i)
#             i += 2
#
#
# solutia = Tree(6)
# print(solutia.baza())

# 5. Circle, cu proprietatea radius, si metodele area() si perimeter().
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         pi = 3.14
#         return pi * (self.radius * self.radius)
#
#     def perimeter(self):
#         pi = 3.14
#         return 2 * pi * self.radius
#
#
# aria_r = Circle(2)
# perimetrul_r = Circle(7)
# print('Aria cercului este: ', aria_r.area())
# print('Perimetrul cercului este: ', perimetrul_r.perimeter())

# 5. - Rectangle, cu proprietatile width, height,
# si metodele area() si perimeter()
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# valori = Rectangle(20, 30)
# print('Aria dreptunghiului este: ', valori.area())
# print('Perimetrul dreptunghiului este: ', valori.perimeter())

# 6. Pyramid, cu propritatile height, base si metoda volume()
# class Pyramid:
#     def __init__(self, height, base):   #base se refera la lungimea unei laturi
#         self.height = height
#         self.base = base
#
#     def volume(self):
#         a = self.base ** 2
#         return (a * self.height) / 3
#
#
# valori = Pyramid(5, 4)
# print('Volumul piramidei este: ', valori.volume())

# 7. Sphere, cu proprietatea radius, si metoda volume().
# class Sphere:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def volume(self):
#         pi = 3.14
#         return 4 / 3 * pi * ((self.radius) ** 3)    #calculul volumului unei sfere
#
#
# volum = Sphere(2)
# print('Volumul sferei este: ', volum.volume())

# 8. Sorter, cu o lista de valori ca proprietate, si o metoda sort() care intoarce lista sortata.
# class Sorter:
#     def __init__(self):
#         self._x = [1, 5, 2, 3, 4, 45, 8, 9, 10, 50]
#
#     def sort(self):
#         sortarea = sorted(self._x)
#         return sortarea
#
#
# rezultat = Sorter()
# print('Lista a fost sortata: ', rezultat.sort())

# 9. Product, care sa aibe proprietatile necesare pentru
# afisarea intr-un e-shop la alegere (titlu, descriere, pret, altele).
# class Product:
#     def __init__(self, titlu, pret, culoare, marime):
#         self.titlu = titlu
#         self.pret = pret
#         self.culoare = culoare
#         self.marime = marime
#
#     def __str__(self):
#         return f'{self.titlu} {self.pret} {self.culoare} {self.marime}'
#
#
# produs_1 = Product('Adidasi', 200.40, 'negru', '40')
# produs_2 = Product('Pantofi', 100, 'rosu', '37')
# print(produs_1)
# print(produs_2)
