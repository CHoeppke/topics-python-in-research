#!/usr/bin/python3
import numpy as np
import urllib
import urllib.request
print("This script is here to solve the exercises")


def findzeros(a, b, c):
    """ Find the real roots of "ax^2 + bx + c"""
    root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    print("The roots are {} and {}".format(root1, root2))
    return (root1, root2)


print(findzeros.__doc__)
(r1, r2) = findzeros(1, 2, 4)

# Urllib exercise:
print("\n Urllib exercise")


def getURL(url="http://www.cam.ac.uk/"):
    data = []
    with urllib.request.urlopen(url) as response:
        charset = response.headers.get_content_charset()
        for line in response:
            data.append(line.decode(charset) + "\n")
    return data


myData = getURL()
print(myData)


# Multiply exercise:
print("\nMultiply exercise")


def multiply(*args):
    res = 1
    for a in args:
        res = res * a

    return res


print(multiply(), " Expected: 1")
print(multiply(1), " Expected: 1")
print(multiply(2), " Expected: 2")
print(multiply(1, 2, 3), " Expected: 6")
print(multiply(42, 42), " Expected: 1764")


def function_with_kwargs(**kwargs):
    for key in kwargs:
        print("The key {key} has the value {value}.".format(key=key, value = kwargs[key]))
    return

function_with_kwargs(foo=8, bar="9", foobar="4"*5)

# Function with many arguments:

def many_args(a, b, c=42, d=0, *e, **f):
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    print("d = " + str(d))

    for i, E in enumerate(e):
        print("e[{}] = {}".format(i, E))

    for key in f:
        print("f[{}] = {}".format(str(key), str(f[key])))


many_args(1, 2, d=3, c=4, bar=8, foo=10)

# Random Walkers exercise
print("Random Walker exercise:")


def getRandomCoordinates():
    c1 = np.random.randint(0, 10)
    c2 = np.random.randint(0, 10)
    return [c1, c2]


def randmove(walker):
    hasmoved = False
    while(not hasmoved):
        xmove = np.random.randint(-1, 2)
        ymove = np.random.randint(-1, 2)
        if(walker[0] + xmove >= 0 and walker[0] + xmove <= 10):
            if(walker[1] + ymove >= 0 and walker[1] + ymove <= 10):
                walker[1] = walker[1] + ymove
                walker[0] = walker[0] + xmove
                hasmoved = True
    return walker


w1 = getRandomCoordinates()
w2 = getRandomCoordinates()
W1moves = [w1]
W2moves = [w2]

while(not w1 == w2):
    w1 = randmove(w1)
    w2 = randmove(w2)
    W1moves.append(w1.copy())
    W2moves.append(w2.copy())

print("Here is how the walkers have moved")
# print("Walker1:" + str(W1moves))
# print("Walker2:" + str(W2moves))

