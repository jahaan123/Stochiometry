import re
from sympy import Matrix, lcm
from tkinter import *

elementList = []
elementMatrix = []

reactantsE = ""
productsE = ""


def addToMatrix(element, index, count, side):
    if (index == len(elementMatrix)):
        elementMatrix.append([])
        for x in elementList:
            elementMatrix[index].append(0)
    if (element not in elementList):
        elementList.append(element)
        for i in range(len(elementMatrix)):
            elementMatrix[i].append(0)
    column = elementList.index(element)
    elementMatrix[index][column] += count * side


def findElements(segment, index, multiplier, side):
    elementsAndNumbers = re.split('([A-Z][a-z]?)', segment)
    i = 0
    while (i < len(elementsAndNumbers) - 1):  # last element always blank
        i += 1
        if (len(elementsAndNumbers[i]) > 0):
            if (elementsAndNumbers[i + 1].isdigit()):
                count = int(elementsAndNumbers[i + 1]) * multiplier
                addToMatrix(elementsAndNumbers[i], index, count, side)
                i += 1
            else:
                addToMatrix(elementsAndNumbers[i], index, multiplier, side)


def compoundDecipher(compound, index, side):
    segments = re.split('(\([A-Za-z0-9]*\)[0-9]*)', compound)
    for segment in segments:
        if segment.startswith("("):
            segment = re.split('\)([0-9]*)', segment)
            multiplier = int(segment[1])
            segment = segment[0][1:]
        else:
            multiplier = 1
        findElements(segment, index, multiplier, side)


def output(solution, reactants, products):
    coEffi = solution.tolist()
    output = ""
    for i in range(len(reactants)):
        output += str(coEffi[i][0]) + reactants[i]
        if i < len(reactants) - 1:
            output += " + "
    output += " -> "
    for i in range(len(products)):
        output += str(coEffi[i + len(reactants)][0]) + products[i]
        if i < len(products) - 1:
            output += " + "
    return output


def main(reactants, products, elementMatrix):
    reactants = reactants.replace(' ', '').split("+")
    products = products.replace(' ', '').split("+")
    for i in range(len(reactants)):
        compoundDecipher(reactants[i], i, 1)

    for i in range(len(products)):
        compoundDecipher(products[i], i + len(reactants), -1)

    elementMatrix = Matrix(elementMatrix)
    elementMatrix = elementMatrix.transpose()
    solution = elementMatrix.nullspace()[0]

    multiple = lcm([val.q for val in solution])
    solution = multiple * solution

    return output(solution, reactants, products)


def getEntries():
    reactantsE = reac.get()
    productsE = prod.get()

    final = Label(root, text=main(reactantsE, productsE, elementMatrix))
    final.grid(column=1, row=3)

    reac.delete(0, END)
    prod.delete(0, END)
    elementList.clear()
    elementMatrix.clear()


root = Tk()

Label(root, text="Reactants: ").grid(column=0, row=0)
reac = Entry(root, width=40)
Label(root, text="Products: ").grid(column=0, row=2)
prod = Entry(root, width=40)

reac.grid(column=1, row=0)
prod.grid(column=1, row=2)

submit = Button(root, text="Balance", command=getEntries).grid(column=2, row=1)

root.mainloop()