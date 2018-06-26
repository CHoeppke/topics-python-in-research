#!/usr/bin/python3
import numpy as np
import scipy
import scipy.fftpack

# Hello World tutorial
print("Hello World")

# Lists:
lista = [1, 2, 66, 4]
listb = lista * 2
print(listb)

listc = lista + [10]
print(listc)


# Floating point maths
if 0.1 + 0.2 == 0.3:
    print("\t"+"Correct Maths")
else:
    print("\t"+"Floating point maths")


# Dictionaries:
print("\n\n")
print("Now dealing with dictionaries")
dict1 = {"key1": 5, "key2": "value2"}
print("\t"+dict1["key2"])
# Can also have integer values as keys
dict2 = {1: 5, '1': "value2"}
print("\t"+str(dict2[1]))
print("\t"+str(dict2['1']))

# Can only use immulatble objects as keys in dicts
# dict3 = {lista: 5, '1': "value2"}

# Adding values to dictionaries:
dict1['key5'] = 25
print("\t"+str(dict1))

# For loops
print("\n\n")
print("Now Dealing with for loops:")
for value in lista:
    print("\t"+str(value))

# Looping through a dictionary
print("\nLooping over a dict")
for (k, v) in dict1.items():
    print("\t"+str(k) + " -> " + str(v))

# Better formatting example
print("\nLooping over a dict with formatting")
for (k, v) in dict1.items():
    mystr = "\tkey {} has the value {}".format(k, v)
    print(mystr)

# Indexing and slicing:
print("\nNow dealing with indexing and slicing")
x = range(10)
print("\t" + str(x[-1]))
print("\t" + str(x[3:7]))

# Using Numpy
print("\nNow using Numpy:")
randarray = np.random.random((2, 3, 4))
print(randarray)

array1 = np.arange(1, 8)
print(array1)

array2 = array1 * 3.7
print(array2)

print("\nNow consider slicing in Numpy")
array3 = np.arange(0, 27).reshape(3, 3, 3)
print(array3)

print(array3[0])
print("\n")
print(array3[0, 1])
print("\n")
print(array3[-1, :, 1:])
print("\n")

array4 = array3 + array3
print(array4)

array5 = array3**3.14159
print(array5)
print("\nSqrt")
print(np.sqrt(array5))
print("\nSin")
print(np.sin(array5))

print("\n\nNow consider matricies")
matrix = np.matrix(array3[0, :, :])
matrix2 = matrix * matrix
print("\nMatrix multiplication")
print(matrix2)

print("\n\nNow using scipy")
print(scipy.fftpack.fftn(array3))

print("\n\nControl statements")
if(5 > 3):
    print("5 is larger than 3")
else:
    print("Maths is broken")

if(1 > 0):
    print("yes, 1 is greater than 0")
elif(1 == 0):
    print("Maths is broken")
else:
    print("Maths is still broken")

# Going back to for loops
print("\n\nNow working with for loops")
# Note that the first index is inclusive and the last one is exclusive.
# This is just one thing python programmers have to remember.
for i in range(4):
    print(str(i))

