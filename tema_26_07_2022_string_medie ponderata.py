'''Tema:
1. Fiind dat un string, sa se afiseze doar consoanele din el.
2. Fiind dat un numar, sa se afiseze divizorii lui.
3. Sa se calculeze produsul tuturor numerelor pare intre 0 si 50.
4. Sa se calculeze media ponderata a 3 variabile a, b, c cu ponderile p1, p2, p3.
5. Fiind dat un numar, sa se afiseze daca este prim sau nu.'''

#Exercitiul 1
# str_dat = 'a, e, i, o , u, k , m, N'
# vocale = str('a, e, i , o, u')
# for char in str_dat:
#     if char not in vocale:
#         print(char)

#Exercitiul 2
# a = 10
# print("Divizorii lui a sunt : ")
# for i in range(1,a + 1):
#     if(a % i == 0):
#         print(i)

#Exercitiul 3 -> Sa se calculeze produsul tuturor numerelor pare intre 0 si 50
# prod = 1
# a = 0
# while a < 50:
#     a += 1
#     if a % 2 == 0:
#         prod *= a
# print(prod)
#Exercitiul 4
# a = 5
# b = 6
# c = 7
# p1 = 10
# p2 = 20
# p3 = 30
# media_ponderata = ((a*p1) + (b*p2) + (c * p3)) / (p1 + p2 + p3)
# print(media_ponderata)

#Exercitiul 5
# z = 11
# if z > 1:
#     for i in range(2, z):
#         if (z % i) == 0:
#             print(z, 'nu este nr prim')
#     else:
#         print(z, 'este nr prim')