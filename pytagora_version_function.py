from math import sqrt

print('** This program calculates the Pythagorean theorem for the triangle ABC with the hypotenuse on side c. **')

side = input('Please enter one of sides a, b or c:')


def getLength():
    return float(input('Please enter the lengths of b and c: '))


def calcTriangle(b, c):
    return sqrt((c ** 2) - (b ** 2))


def calcTriangle2(a, c):
    return sqrt((c ** 2) - (a ** 2))


def calcTriangle3(a, b):
    return sqrt((a ** 2) + (b ** 2))


if side == 'a':

    b = getLength()
    c = getLength()

    print('The length of your third side is: ', calcTriangle(b, c))

elif side == 'b':

    a = getLength()
    c = getLength()

    print('The length of your third side is: ', calcTriangle2(a, c))


elif side == 'c':

    a = getLength()
    b = getLength()

    print('The length of your third side is: ', calcTriangle3(a, b))


else:
    print('INVALID INPUT! Please enter one of sides a, b or c: ')
