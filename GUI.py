from tkinter import *
from tkinter import ttk
import balancer

elementMatrix = []
elementList = []

reactants = ""
products = ""

def getEntries():
    reactants = reac.get()
    products = prod.get()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Reactants: ").grid(column=0, row=0)
reac = ttk.Entry(frm, width=40).grid(column=1, row=0)


ttk.Label(frm, text="Products: ").grid(column=0, row=2)
prod = ttk.Entry(frm, width=40).grid(column=1, row=2)

ttk.Button(frm, text="Balance", command=getEntries).grid(column=2, row=1)

print(balancer.main(reactants, products, elementMatrix))

root.mainloop()