from tkinter import *

class Calculator():
    def __init__(self):
        self.phase1 = 0 
        self.phase2 = 0 
        self.final = 0 
        self.entry = StringVar()
        self.text = "" 
        self.signe = "" 
        self.entry.set("Calculatrice9000")

    def init(self):
        self.phase1 = 0 
        self.phase2 = 0 
        self.final = 0
        self.text = "" 
        self.signe = ""
    
    def operation(self):
        try:    
            if "+" in self.text:
                self.plus()
            elif "-" in self.text:
                self.moins()
            elif "x" in self.text:
                self.multi()
            elif "/" in self.text:
                self.div()
            elif "%":
                self.reste()
        except:
            self.entry.set("Erreur")
            self.init

    def plus(self):
        nombre=self.text.split("+")
        self.partie1= float(nombre[0])
        self.partie2= float(nombre[1])
        self.result= self.partie1 + self.partie2
        self.entry.set(str(self.result))
        self.init()
    
    def moins(self):
        nombre=self.text.split("-")
        self.partie1= float(nombre[0])
        self.partie2= float(nombre[1])
        self.result= self.partie1 - self.partie2
        self.entry.set(str(self.result))
        self.init()
    
    def multi(self):
        nombre=self.text.split("x")
        self.partie1= float(nombre[0])
        self.partie2= float(nombre[1])
        self.result= self.partie1 * self.partie2
        self.entry.set(str(self.result))
        self.init()
    
    def div(self):
        nombre=self.text.split("/")
        self.partie1= float(nombre[0])
        self.partie2= float(nombre[1])
        self.result= self.partie1 / self.partie2
        self.entry.set(str(self.result))
        self.init()
    
    def reste(self):
        nombre=self.text.split("%")
        self.partie1= float(nombre[0])
        self.partie2= float(nombre[1])
        self.result= self.partie1 % self.partie2
        self.entry.set(str(self.result))
        self.init()
    


def Button0():
    calculatrice.text += '0'
    calculatrice.entry.set(calculatrice.text)

def Button1():
    calculatrice.text += '1'
    calculatrice.entry.set(calculatrice.text)

def Button2():
    calculatrice.text += '2'
    calculatrice.entry.set(calculatrice.text)

def Button3():
    calculatrice.text += '3'
    calculatrice.entry.set(calculatrice.text)

def Button4():
    calculatrice.text += '4'
    calculatrice.entry.set(calculatrice.text)

def Button5():
    calculatrice.text += '5'
    calculatrice.entry.set(calculatrice.text)

def Button6():
    calculatrice.text += '6'
    calculatrice.entry.set(calculatrice.text)

def Button7():
    calculatrice.text += '7'
    calculatrice.entry.set(calculatrice.text)

def Button8():
    calculatrice.text += '8'
    calculatrice.entry.set(calculatrice.text)
    
def Button9():
    calculatrice.text += '9'
    calculatrice.entry.set(calculatrice.text)

def ButtonPlus():
    calculatrice.text += '+'
    calculatrice.entry.set(calculatrice.text)

def ButtonMoins():
    calculatrice.text += '-'
    calculatrice.entry.set(calculatrice.text)

def ButtonDiviser():
    calculatrice.text += '/'
    calculatrice.entry.set(calculatrice.text)

def ButtonMultiplication():
    calculatrice.text += 'x'
    calculatrice.entry.set(calculatrice.text)

def ButtonReste():
    calculatrice.text += '%'
    calculatrice.entry.set(calculatrice.text)

def ButtonVirgule():
    calculatrice.text += '.'
    calculatrice.entry.set(calculatrice.text)

def ButtonRéinitialisation():
    calculatrice.text = ''
    calculatrice.entry.set(calculatrice.text)

def ButtonEgal():
    calculatrice.operation()



fen = Tk()
fen.geometry("200x260") 
fen.title("Calculatrice9000")
fen["bg"]= "white"
calculatrice = Calculator()

Ecran=Entry(fen, width=28, textvariable=calculatrice.entry, bg ="black", fg="white", bd=5).place(x=9, y=8)

B1 = Button(fen, text="1", command=Button1, width=3, height=2, bg="white", fg="black").place(x=10, y=40)
B2 = Button(fen, text="2", command=Button2, width=3, height=2, bg="white", fg="black").place(x=50, y=40)
B3 = Button(fen, text="3", command=Button3, width=3, height=2, bg="white", fg="black").place(x=90, y=40)
B4 = Button(fen, text="4", command=Button4, width=3, height=2, bg="white", fg="black").place(x=10, y=90)
B5 = Button(fen, text="5", command=Button5, width=3, height=2, bg="white", fg="black").place(x=50, y=90)
B6 = Button(fen, text="6", command=Button6, width=3, height=2, bg="white", fg="black").place(x=90, y=90)
B7 = Button(fen, text="7", command=Button7, width=3, height=2, bg="white", fg="black").place(x=10, y=140)
B8 = Button(fen, text="8", command=Button8, width=3, height=2, bg="white", fg="black").place(x=50, y=140)
B9 = Button(fen, text="9", command=Button9, width=3, height=2, bg="white", fg="black").place(x=90, y=140)
B0 = Button(fen, text="0", command=Button0, width=3, height=2, bg="white", fg="black").place(x=50, y=190)
BF = Button(fen, text=".", command=ButtonVirgule, width=3, height=2, bg="lightgrey", fg="black").place(x=90, y=190)
BC = Button(fen, text="C", command=ButtonRéinitialisation, width=3, height=2, bg="gold", fg="red",).place(x=10, y=190)
BP = Button(fen, text="+", command=ButtonPlus, width=3, height=1, bg="lightgrey", fg="black").place(x=150, y=40)
BS = Button(fen, text="-", command=ButtonMoins, width=3, height=1, bg="lightgrey", fg="black").place(x=150, y=75)
BD = Button(fen, text="/", command=ButtonDiviser, width=3, height=1, bg="lightgrey", fg="black").place(x=150, y=110)
BM = Button(fen, text="X", command=ButtonMultiplication, width=3, height=1, bg="lightgrey", fg="black").place(x=150, y=145)
BM = Button(fen, text="%", command=ButtonReste, width=3, height=1, bg="lightgrey", fg="black").place(x=150, y=180)
BE = Button(fen, text="=", command=ButtonEgal, width=3, height=1, bg="lightgrey", fg="black").place(x=150, y=220)

fen.mainloop()