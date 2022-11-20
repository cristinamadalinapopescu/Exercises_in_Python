#Fiind data o temperatura sa se afiseze unul dintre urmatoarele mesaje: <0 e inghtetat trebuie geaca, 0 < 20 trebuie bluza, 20 < merge tricou
# if si elif
# temperatura = int(input("Introduceti temperatura: "))
# if temperatura < 0:
#     print("E inghetat, trebuie geaca!")
# elif 0 < temperatura < 20:
#     print("E frig, trebuie bluza!")
# else:
#     print("E cald, merge tricou!")


# Sa se afiseze toate numerele impare intre 0 si 100.
# a = 0
# while a < 100:
#     a += 1
#     if a % 2 != 0:
#         print(a)
#
# #Sa se calculeze suma tuturor numerelor intre 0 si 500.
# suma = 0
# a = 0
# while a <= 500:
#     suma += a
#     a += 1
# print(suma)

#Sa se genereze primele 50 de numere din sirul lui Fibonacci.
# fib = [1, 1, 2, 3, 5, 8 ,13, 21,...] <- sirul lui Fibonacci
#poate sa inceapa si de la 0, nu neaparat 1, pt ca 0+1=1 si tot de la 1 incepe practic sirul
# a = 0
# b = 1
# print(a)
# print(b)
# fib_count = 0
# while fib_count < 50:
#     fib_count += 1
#     print(a+b)
#     c = a + b
#     a = b
#     b = c

## Cu dimensiunea bazei luata dintr-o variabila:
# a) Sa se afiseze in terminal o jumatate de brad de forma urmatoare

#  #
#  ##
#  ###
#  ####
#  #####
#  ######

# i = 0
# var = 5
# while i < var:
#     i += 1
#     print('#' * i)

# b) Sa se afiseze un brad de forma:

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

# c) Sa se afiseze un brad cu cer de forma: "TEMA"

# ^^^^ # ^^^^
# ^^^ ### ^^^
# ^^ ##### ^^
# ^ ####### ^
#  #########
# ###########

#Fiind dat un numar intreg, sa se calucleze suma cifrelor.
# numar = 74
# suma = 0
# while numar != 0:
#     cifra = numar % 10
#     suma += cifra
#     numar = numar // 10
#
# print(suma)

#EXERCITIUL DE SUS SE MAI POATE REZOLVA ASTFEL:
# suma = 0
# numar = '74'
# for cifra_str in numar:
#     cifra = int(cifra_str)
#     suma += cifra
#
# print(suma)


