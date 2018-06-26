#!/usr/bin/python3
import numpy as np
# Solves the exercise on classes

class AnimalClass():

    def __init__(self, name):
        self.name = name
        self.children = []

    def getName(self):
        return self.name

    def addChildren(self, child):
        self.children.append(child)

    def getTree(self):
        lines = []
        lines.append(self.name)
        for child in self.children:
            childlines = child.getTree()
            lines.append("|---> " + child.getName())
            for idx in range(1, len(childlines)):
                childline = childlines[idx]
                lines.append("|\t" + childline)
        return lines


# Generate the Classes from the exercise
Animal = AnimalClass("Animal")
Mamal = AnimalClass("Mamal")
Cow = AnimalClass("Cow")
Koala = AnimalClass("Koala")
Human = AnimalClass("Human")
ChuckNorris = AnimalClass("Chuck Norris")
Fish = AnimalClass("Fish")
Mackarel = AnimalClass("Mackarel")
Salmon = AnimalClass("Salmon")
Bird = AnimalClass("Bird")
Magpie = AnimalClass("Magpie")
Owl = AnimalClass("Owl")

Human.addChildren(ChuckNorris)
Mamal.addChildren(Cow)
Mamal.addChildren(Koala)
Mamal.addChildren(Human)
Fish.addChildren(Mackarel)
Fish.addChildren(Salmon)
Bird.addChildren(Magpie)
Bird.addChildren(Owl)

Animal.addChildren(Mamal)
Animal.addChildren(Fish)
Animal.addChildren(Bird)

Tree = Animal.getTree()
for l in Tree:
    print(l)
