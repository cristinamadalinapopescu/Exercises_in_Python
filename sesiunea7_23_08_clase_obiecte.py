d# CLASE SI OBIECTE

# class Produs:
#     def __init__(self):
#         self.nume = ''  # proprietate
#         self.descriere = ''  # proprietate
#         self.pret = 0  # proprietate
#
#     def afisare(self):  # metoda
#         print(f'{self.nume} {self.pret}')
#
#
# un_produs = Produs()
# un_produs.nume = 'HP'
# un_produs.descriere = 'Pavillion dv5'
# un_produs.pret = 899.98
# print(un_produs.nume)
# un_produs.afisare()
########################################
# class Produs:
#     def __init__(self, nume, pret):  # constructor, sau initializer
#         self.nume = nume  # proprietate
#         self.descriere = ''  # proprietate
#         self.pret = pret  # proprietate
#
#     def __str__(self):  # metoda apelata cand un obiect ia forma de string
#         return f'{self.nume} {self.pret}' # returneaza un string
#
#     def __repr__(self):  # metoda apelata cand un obiect este reprezentat intr-un iterabil
#         return f''  # returneaza un string
#
#     def __len__(self):  # metoda __len__ este apelata cand un obiect este dat ca parametru functiei len()
#         return 0  #
#
#
# p1 = Produs('mere', 12.5)
# print(p1)
# print([p1, ])
# print(len(p1))

####################################
# class Produs:
#     def __abs__(self):
#         pass
#
#     def __lt__(self, other):  # less than
#         pass
#
#     def __le__(self, other):  # less than or equal
#         pass
#
#     def __gt__(self, other):  # greater than
#         pass
#
#     def __ge__(self, other):  # greater than or equal
#         pass
#
#     def __float__(self):  # ce forma sa ia cand obiectul e dat ca parametru functiei float
#         pass

#################################################
# class Produs:
#     def __init__(self, nume, pret, descriere=''):  # constructor, sau initializer
#         self.nume = nume  # proprietate
#         self.descriere = descriere  # proprietate
#         self.pret = pret  # proprietate
#
#     def __str__(self):  # metoda apelata cand un obiect ia forma de string
#         return f'{self.nume} {self.pret}'  # returneaza un string
#
#     def __repr__(self):  # metoda apelata cand un obiect este reprezentat intr-un iterabil
#         return f''  # returneaza un string
#
#     def __len__(self):  # metoda __len__ este apelata cand un obiect este dat ca parametru functiei len()
#         return 0  #
#
#     def __abs__(self):
#         pass
#
#     def __lt__(self, other):  # less than
#         # return len(self.nume) < len(other.nume)  # compara lungimea titlului
#         return self.pret < other.pret  # compara pretul
#
#     def __le__(self, other):  # less than or equal
#         pass
#
#     def __gt__(self, other):  # greater than
#         pass
#
#     def __ge__(self, other):  # greater than or equal
#         pass
#
#     def __float__(self):  # ce forma sa ia cand obiectul e dat ca parametru functiei float
#         pass
#
#
# p1 = Produs('mere', 12.5)
# # print(p1)
# # print([p1, ])
# # print(len(p1))
# p2 = Produs('alune', 15)
# print(p1 < p2)
#################################################
# class Produs:
#     def __init__(self, nume):
#         self._nume = nume
#
#     def get_nume(self):     #exercitiul asta e ceva explicatie by Tavi in video din 23-08-2022
#         return self._nume


# p1 = Produs('mere')
# print(p1.get_nume())
# print(p1._nume)

#####################################

# Exercitiul 1:
# Sa se scrie o clasa Cetatean cu nume, prenume, cnp.
# class Cetatean:
#     def __init__(self, nume, prenume, cnp):
#         self.nume = nume
#         self.prenume = prenume
#         self.cnp = cnp
#
#     def __str__(self):
#         return f'{self.prenume} {self.nume}'
#
#
# ion = Cetatean('Ionescu ', 'Ion', '18523257655')
# gheorghe = Cetatean('Georgescu', 'Gheorghe', '1258762665')
#
# print(ion)
# print(gheorghe)

###########################################
# EXERCITIUL 2:
'''Fiind date clasele Cetatean si Locatar,
 sa se scrie o noua clasa Rezident care sa mosteneasca din ambele.'''


# class Cetatean:
#     def __init__(self, nume, prenume, cnp):
#         self.nume = nume
#         self.prenume = prenume
#         self.cnp = cnp
#
#     def __str__(self):
#         return f'{self.prenume} {self.nume}'
#
#
# # Adaugati pe Locatar oras, strada, numar, aparatament.
# class Locatar:
#     def __init__(self, oras, strada, numar, apartament):
#         self.oras = oras
#         self.strada = strada
#         self.numar = numar
#         self.apartament = apartament
#
#     def __str__(self):
#         return f'{self.oras} {self.strada} {self.numar} {self.apartament}'
#
#
# bucuresti = Locatar('Bucuresti', 'Florilor', '23', '12')
# print(bucuresti)

#
# class Rezident(Cetatean, Locatar):
#     def __init__(self, nume, prenume, cnp):
#         super().__init__(nume, prenume, cnp)

