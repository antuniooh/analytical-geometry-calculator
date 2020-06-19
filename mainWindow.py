from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox 

import os

from modules import position
from modules import graph
from modules import distance

def show():
    u = []
    n = []
    A = []
    B = []
    a = 1
    b = 1
    c = 1 
    d = 1
    
    window = Tk()
    window.title("Calculadora Vetores")
    window.geometry('870x600')

    xPoint1 = Entry(window, width=14,font=("Arial",11))
    xPoint1.place(x=50, y=40)
    yPoint1 = Entry(window, width=14,font=("Arial",11))
    yPoint1.place(x=50, y=80)
    zPoint1 = Entry(window, width=14,font=("Arial",11))
    zPoint1.place(x=50, y=120)

    xPoint2 = Entry(window, width=14,font=("Arial",11))
    xPoint2.place(x=50, y=180)
    yPoint2 = Entry(window, width=14,font=("Arial",11))
    yPoint2.place(x=50, y=220)
    zPoint2 = Entry(window, width=14,font=("Arial",11))
    zPoint2.place(x=50, y=260)

    stretchA = Entry(window, width=14,font=("Arial",11))
    stretchA.place(x=50, y=320)
    stretchB = Entry(window, width=14,font=("Arial",11))
    stretchB.place(x=50, y=360)
    stretchC = Entry(window, width=14,font=("Arial",11))
    stretchC.place(x=50, y=400)
    stretchD = Entry(window, width=14,font=("Arial",11))
    stretchD.place(x=50, y=440)

    label = Label(window, text="Selecione o cálculo desejado...", font=("Arial", 12),width=100)
    label.place(x = 370, y = 40)

    def setValues():
        A = [int(xPoint1.get()), int(yPoint1.get()),int(zPoint1.get())]
        B = [int(xPoint2.get()), int(yPoint2.get()),int(zPoint2.get())]

        u = [int(B[0]) - int(A[0]), int(B[1]) - int(A[1]),int(B[2]) - int(A[2])] # b-a

        a = int(stretchA.get())
        b = int(stretchB.get())
        c =  int(stretchC.get())
        d =  int(stretchD.get())
        n = [a, b, c]

    def position():
        setValues()
        pos = (u[0]*n[0] + u[1]*n[1] + u[2]*n[2])
        posicao = position.Posicao(a, b, c, d,u, pos)
        res = messagebox.showinfo("Resultado",posicao)
        print(res)
        
    def distance():
        setValues()
        pos = (u[0]*n[0] + u[1]*n[1] + u[2]*n[2])

        posicao = position.Posicao(a, b, c, d,u, pos)
        distancia = distance.Distancia(a, b, c, d, A,B, posicao)
        
        res = messagebox.showinfo("Resultado",distancia)
        print(res)

    def graph():
        setValues()
        graph.Grafico(A,B,n,d)

    def calc():
        result = ""
        setValues()

        result+=("A reta obtida e: %s + t %s \n" % ( A,u))
        result+=("Equacao Vetorial:")
        result+=("X = " + str(A[0]) + "+ (" + str(u[0]) + ")t")
        result+=("Y = " + str(A[1]) + "+ (" + str(u[1]) + ")t")
        result+=("Z = " + str(A[2]) + "+ (" + str(u[2]) + ")t")
        result+=("")

        result+=("A equacao obtida e: " +  str(a) + "x + " + str(b) + "y + " + str(c) + "z + " + str(d) + "\n")
        result+=("Vetor N obtido: %s \n" %n)
        result+=("")

        label['text'] = result

    btn1 = Button(window, text = "Posição Relativa", command = position)
    btn1.place(x = 380, y = 80)
    btn2 = Button(window, text = "Distancia", command = distance)
    btn2.place(x = 380, y = 120)
    btn3 = Button(window, text = "Gráfico", command = graph)
    btn3.place(x = 380, y = 160)
    btn4 = Button(window, text = "Iniciar Calculos...", command = calc)
    btn4.place(x = 380, y = 200)

    label = Label(window)
    label.place(x = 50, y = 170)

    window.mainloop()