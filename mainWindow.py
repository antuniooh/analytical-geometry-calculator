from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox 

import os

from modules import position
from modules import graph
from modules import distance

def show():
    window = Tk()
    window.title("Calculadora Vetores")
    window.geometry('430x350')

    labelPoint1 = Label(window, text= "Ponto 1", font=("Arial", 16))
    labelPoint1.place(x=80, y=20)
    labelPoint2 = Label(window, text= "Ponto 2", font=("Arial", 16))
    labelPoint2.place(x=280, y=20)
    labelStretch = Label(window, text= "Equação de reta", font=("Arial", 16))
    labelStretch.place(x=50, y=100)

    xPoint1 = Entry(window, width=5,font=("Arial",11))
    xPoint1.place(x=50, y=60)
    yPoint1 = Entry(window, width=5,font=("Arial",11))
    yPoint1.place(x=100, y=60)
    zPoint1 = Entry(window, width=5,font=("Arial",11))
    zPoint1.place(x=150, y=60)

    xPoint2 = Entry(window, width=5,font=("Arial",11))
    xPoint2.place(x=250, y=60)
    yPoint2 = Entry(window, width=5,font=("Arial",11))
    yPoint2.place(x=300, y=60)
    zPoint2 = Entry(window, width=5,font=("Arial",11))
    zPoint2.place(x=350, y=60)

    stretchA = Entry(window, width=5,font=("Arial",11))
    stretchA.place(x=50, y=140)
    stretchB = Entry(window, width=5,font=("Arial",11))
    stretchB.place(x=100, y=140)
    stretchC = Entry(window, width=5,font=("Arial",11))
    stretchC.place(x=150, y=140)
    stretchD = Entry(window, width=5,font=("Arial",11))
    stretchD.place(x=200, y=140)


    def calculateValues():
        A = [int(xPoint1.get()), int(yPoint1.get()),int(zPoint1.get())]
        B = [int(xPoint2.get()), int(yPoint2.get()),int(zPoint2.get())]

        u = [int(B[0]) - int(A[0]), int(B[1]) - int(A[1]),int(B[2]) - int(A[2])] # b-a

        a = int(stretchA.get())
        b = int(stretchB.get())
        c =  int(stretchC.get())
        d =  int(stretchD.get())
        n = [a, b, c]

        return A, B, u, n, a, b, c, d

    def positionCalc():
        A, B, u, n, a, b, c, d = calculateValues()

        pos = (u[0]*n[0] + u[1]*n[1] + u[2]*n[2])
        posicao = position.Posicao(a, b, c, d,u, pos)
        res = messagebox.showinfo("Resultado",posicao)
        print(res)

        return posicao
        
    def distanceCalc():
        A, B, u, n, a, b, c, d = calculateValues()

        distancia = distance.Distancia(a, b, c, d, A,B, positionCalc())
        
        res = messagebox.showinfo("Resultado",distancia)
        print(res)

    def graphCalc():
        A, B, u, n, a, b, c, d = calculateValues()
        graph.Grafico(A,B,n,d)

    def calc():
        A, B, u, n, a, b, c, d = calculateValues()

        result = ""

        result+=("A reta obtida e: %s + t %s \n\n" % ( A,u))
        result+=("Equacao Vetorial:\n")
        result+=("X = " + str(A[0]) + "+ (" + str(u[0]) + ")t\n")
        result+=("Y = " + str(A[1]) + "+ (" + str(u[1]) + ")t\n")
        result+=("Z = " + str(A[2]) + "+ (" + str(u[2]) + ")t\n")
        result+=("\n")

        result+=("A equacao obtida e: " +  str(a) + "x + " + str(b) + "y + " + str(c) + "z + " + str(d) + "\n\n")
        result+=("Vetor N obtido: %s \n\n" %n)
        result+=("")

        res = messagebox.showinfo("Resultado",result)
        print(res)

    btn1 = Button(window, text = "Posição Relativa", command =  positionCalc)
    btn1.place(x = 50, y =200)
    btn2 = Button(window, text = "Distancia", command = distanceCalc)
    btn2.place(x = 190, y = 200)
    btn3 = Button(window, text = "Gráfico", command = graphCalc)
    btn3.place(x = 280, y = 200)
    btn4 = Button(window, text = "Calcular reta e equação...", command = calc)
    btn4.place(x = 50, y = 240)

    window.mainloop()