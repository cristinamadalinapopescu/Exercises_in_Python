'''Sa se scrie o functie care intoarce media armonica a oricator parametri obligatorii'''
# def media_armonica(*n):
# 	n2 = 0
# 	total = 0
# 	while n2 < (len(n)):
# 		total = total + (1/n[n2])
# 		n2+=1
# 	total = len(n)/total
# 	return total
#
# print(media_armonica(1,2,3,4,5,6))

'''Sa se scrie o functie care primeste un numar ca parametru, si intoarce factorialul acestuia'''
# Python program to find the factorial of a number provided by the user.

# To take input from the user
# num = int(input("Enter a number: "))
#
# factorial = 1
#
# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

'''Sa se scrie o functie care primeste o raza si intoarce aria cercului cu respectiva raza'''
# def raza_cercului(r):
# 	p = 3.14
# 	return(p*(r**2))
#
# print(raza_cercului(5))

'''Sa se scrie o functie care primeste o temperatura in grade celsius, si intoarce valoarea in fahrenheit'''

# def celsius(a):
# 	f = a*1.8+32
# 	return(f)
#
# print(celsius(10))

'''Fiind date posibilitatile ╲ │ ╱ ─ , scrieti o functie care sa primeasca un parametru string de forma
"╲││╱│─╱││─╱╲│─│─╲╲╱╱││─╱│╲─╱─"
si care sa returneze un string cu fiecare caracter intors 45' la dreapta. (\ -> |, | -> /)'''

# def string_la_45(*args: str):
#     dict_posib = {"╲": '│', '│': '╱', '╱': '─', '─': '╲'}
#     rotated = [dict_posib[i] for i in list(*args)]
#
#     print(rotated)
#     result = ''
#     for value in rotated:
#         result += value
#
#     return result
#
#
# string = '╲││╱│─╱││─╱╲│─│─╲╲╱╱││─╱│╲─╱─'
# print(string)
# print(string_la_45(string))

'''Scrieti o functie care primeste o lista de dictionare cu cate 3 chei,
si afiseaza valorile din dictionar pe cate o coloana a tabelului.'''


def display_row(value_dict, start_div="║", end_div="║", mid_div="║", line_length=79, is_header=False):
    print_err = line_length // len(value_dict) - 1
    print(start_div, end='')
    for index, key in enumerate(value_dict.keys()):
        if not is_header:
            key = value_dict[key]
        print(key.ljust(print_err), end=mid_div if index != len(value_dict) - 1 else '')
    print(end_div)


def display_table(*args, line_length=79):
    for index, value_dict in enumerate(*args):
        print_column_length = line_length // len(value_dict) - 1
        # print(value_dict)
        if index == 0:
            print("╔" + "═" * print_column_length + "╦" + "═" * print_column_length + "╗")
            display_row(value_dict, line_length=line_length, is_header=True)
        display_row(value_dict, line_length=line_length)
        if index == len(value_dict):
            print("╚" + "═" * print_column_length + "╩" + "═" * print_column_length + "╝")


# main function
all_option_dict = [
    {'Opt. no.': '1', 'Req': 'Symbol rotation'},
    {'Opt. no.': '2', 'Req': 'Factorial functions'},  # optional
    {'Opt. no.': '3', 'Req': 'Harmonic Mean'},  # optional
]
display_table(all_option_dict)