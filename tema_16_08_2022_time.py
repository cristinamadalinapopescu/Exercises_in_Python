'''Sa se scrie o functie care primeste ca parametri 2 intregi start_hour (ex. 9)
si end_hour (ex. 17), si genereaza o lista
 de string-uri de intervale orare: ['9:00 - 10:00', '10:00 - 11:00', ..., '16:00 - 17:00'. '''

# def interval_orar(start, final):
#     return [f'{i}:00 - {i + 1}:00' for i in range(start, final)]
#
#
# print(interval_orar(9, 17))

'''Sa se scrie o functie care primeste un string, si il valideaza ca ora valida hh:mm de forma '23:59' (adica functia
 intoarce un boolean, True daca e ora valida in string, False daca nu).'''

# import time
#
#
# def is_hh_mm_time(time_string):
#     try:
#         time.strptime(time_string, '%H:%M')
#     except ValueError:
#         return False
#     return len(time_string) == 5
#
#
# time_string = input('Stringul meu este: ')
# time.strptime('08:30', '%H:%M')
# print(is_hh_mm_time(time_string))

'''Sa se scrie o functie care primeste un string,
si il valideaza ca data valida zz/ll/aaaa de forma '31/12/2022'.'''


# MONTHS_31 = ('01', '03', '05', '07', '08', '10', '12')
# MONTHS_30 = ('04', '06', '09', '11')
#
#
# def is_leap_year(year):
#     year = int(year)
#     return ((year % 400 == 0) and (year % 100 == 0)) or ((year % 4 == 0) and (year % 100 != 0))
#
#
# def validare_format_data(zi_luna_an):
#     day = zi_luna_an[:2]
#     month = zi_luna_an[3:5]
#     year = zi_luna_an[6:]
#
#     day_31_valid = month in MONTHS_31 and 1 <= int(day) <= 31
#     day_30_valid = month in MONTHS_30 and 1 <= int(day) <= 30
#     day_feb29_valid = is_leap_year(year) and month == '02' and 1 <= int(day) <= 29
#     day_feb28_valid = month == '02' and 1 <= int(day) <= 28
#
#     year_valid = int(year) >= 1900
#     month_valid = 1 <= int(month) <= 12
#     day_valid = day_31_valid or day_30_valid or day_feb29_valid or day_feb28_valid
#
#     return year_valid and month_valid and day_valid
#
#
# print(validare_format_data('29/02/2000'))

# 1. Conversia unei temperaturi din 'C in 'F.
# def celsius(a):
# 	f = a*1.8+32
# 	return(f)
#
# print(celsius(10))

# 2. Conversia unei temperaturi din 'F in 'C.
# def fahren(f):
# 	a = (f-32)/1.8
# 	return(a)
#
# print(fahren(50))

# 3.Produsul tuturor numerelor de la 1 pana la o valoare primita ca parametru.
# def produsul_pana_la(numar):
#
#     if numar == 1:
#         return numar
#     else:
#         return numar * produsul_pana_la(numar - 1)
#
#
# print(produsul_pana_la(5))

# 4. Media armonica a oricator valori primite prin parametru.
# def media_armonica(*a):
# 	b = 0
# 	suma = 0
# 	while b < (len(a)):
# 		suma = suma + (1/a[b])
# 		b+=1
# 	suma = len(n)/suma
# 	return suma
#
# print(media_armonica(1,2,3,4,5,6))

# 5. Calculul ariei unui cerc, cu raza primita prin parametru.
# def aria_cercului(r):
#     pi = 3.14
#     return pi * (r*r)
# print('Aria cercului este:', aria_cercului(2))

# 6. Calculul volumului unei sfere cu raza primita prin parametru.
# def volumul_sferei(r):
#     pi = 3.14
#     return 4/3*pi*3*r**3
# print('The volume of the sphere is: ',volumul_sferei(2))

# 7. Conversia unui string de forma "1.234.567,89 Lei" la un float de forma 1234567.89.
# def variabila(v):
#     return v.replace('.', '').replace(',', '.').replace('Lei', '')
#
#
# print(variabila("1.234.567,89 Lei"))

# 8.Afisarea unui drepunghi umplut cu raracterul '#' in terminal, cu latimea si lungimea date ca parametri.
# def dreptunghi(rows, columns, symbol):
#     for i in range(rows):
#         for j in range(columns):
#             print(symbol, end='')
#         print()
#
#
# r = int(input("Lungimea randului: "))
# c = int(input("Numar coloane: "))
# s = input("Simbolul este: ")
# dreptunghi(r, c, s)

# 9.Reducerea preciziei unui float primit ca parametru la 2 zecimale
# def un_float(f):
#     return round(f,2)       #Apelați round(number, ndigits) cu un float ca număr și 2 ca ndigits pentru a rotunji float la două zecimale.
#
# print(un_float(45.87422))
