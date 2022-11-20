# Sa se scrie un algoritm care asigura citirea unui float de la tastatura.
# In caz ca valoarea este de alt tip decat float, sa se reincerce citirea de la tastatura.

# valoare = input('introduceti float: ')
# while type(valoare) != float:
#     try:
#         valoare = float(valoare)
#     except ValueError:
#         valoare = input('introduceti float: ')

'''Fiind data o lista cu valori, sa se citeasca un index de la tastatura.
Sa se afiseze valoarea de pe indexul citit. In caz ca indexul este invalid, sa se citeasca o alta valoare.'''
# lista_valori = [2, 'abc', 5, 9]
# index = input('index:')
# index_valid = False
# while not index_valid:
#     while type(index) != int:
#         try:
#             index = int(index)
#         except ValueError:
#             index = input('Introduceti index intreg: ')
#     try:
#         print(lista_valori[index])
#         index_valid = True
#     except IndexError:
#         index = input('Introduceti un index valid: ')

# Fiind data ecuatia de grad 1, sa se emita ValueError in caz ca a, b nu sunt valide.
# class FirstDegreeEcuation:
#     def __init__(self, a, b):
#         if a == 0 and b != 0:
#             raise ValueError
#         self.a = a
#         self.b = b
#
#     def solution(self):
#         return -self.b / self.a
#
#
# ec1 = FirstDegreeEcuation(0, 1)

# Sa se implementeze ValueError in SecondDegreeEcuation in caz ca a, b, c sunt invalide.
# class SecondDegreeEcuation:
#     def __init__(self, a, b, c):
#         if a == 0:
#             raise ValueError
#
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def solutii(self):
#         delta = self.b ** 2 - 4 * self.a * self.c
#         if delta >= 0:
#             x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
#             x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
#             return x1, x2
#         else:
#             return None, None
#
#
# ec2 = SecondDegreeEcuation(0,1,1)   #iese:raise ValueError cu (0,1,1)
# print(ec2.solutii())
