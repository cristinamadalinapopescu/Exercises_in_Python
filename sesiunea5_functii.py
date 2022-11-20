# a, b, c = 1, 3, 5
# media = (a + b+ c) / 3
# ceva_text_plus = 'Media aritmetica a lui '+str(a)+' si '+str(b)+' si '+str(c)+' este ' + media
# ceva_text_format = 'Media aritmetica a lui {} si {} si {}'.format(a, b, c, media)
# ceva_text_fstring = f'Media aritmetica a lui {a} si {b} si {c} este {media}'

# def media_aritmetica(a, b)
#     return (a + b) / 2
#
# ma1 = media_aritmetica(2, 3)
# ma2 = media_aritmetica(5, 7)
#
# print(ma1)
# print(ma2)

# def media_artimetica(*args):
#     if len(args) == 0:
#         return None
#     return sum(args) / len(args)
#
#
# print(media_artimetica())
# print(media_artimetica(1, 2, 3, 4, 5, 6))

'''Sa se scrie o functie care primeste oricate parametri mandatory,
si intoarce produsul acestora'''

# def produs(args):
#     p = 1
#     for i, value in enumerate(args):
#         p= value
#         # p *= args[i]
#     return p
#
#
# print(produs(2, 3, 4))

# def afisare_elemente(**kwargs):
#     for key in kwargs:
#         print(key, kwargs[key])
#
#
# afisare_elemente(a=1, b=2, c='maimuta', alt_parametru=True)

'''Sa se scrie o functie care primeste o lista de numere, si intoarce o lista cu 
cuburile numerelor impare din lista initiala (fiecare numar ridicat la puterea 3)'''

# def list_cubes(*args):
#     cuburi = []
#     for value in args:
#         if value % 2 != 0:
#             cub = value ** 3
#             cuburi.append(cub)
#
#     return cuburi
# print(list_cubes(2, 4, 5, 6, 7, 8, 9))

'''Sa se scrie o functie care primeste un parametru string,
si intoarce un dictionar cu perechi litera si numarul de aparitii a literei in cuvant'''
#
def letter_index_2(word2: str):
    rez = {}
    for char in word2:
        rez[char] = word2.count(char)
        return rez

#
#
        return {char:word2.count(char) for char in word}


word = input('Enter a string: ')
print(letter_index_2(word))

#Functii recursive
# def suma_pana_la(numar):
#     if numar == 0:
#         return 0
#     else:
#         return numar + suma_pana_la(numar - 1)
#
#
# print(suma_pana_la(50))



