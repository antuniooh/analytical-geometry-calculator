from math import sqrt
from math import pow
#pip install numpy
import numpy as np
#sudo apt-get install python3-matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 


def Grafico(A,B,N,d):
    x = [A[0], B[0]]
    y = [A[1], B[1]]
    z = [A[2], B[2]]

    reta = plt.figure()

    ax = reta.add_subplot(111, projection='3d')
    ax.plot(x, y, z)

    xx, yy = np.meshgrid(range(10), range(10))
    z = (-N[0] * xx - N[1] * yy - d) * 1. / N[2]
    plt3d = reta.gca(projection='3d')
    plt3d.plot_surface(xx, yy, z)
    plt.show()

def Posicao(a, b, c, d,u, pos):
    posicao =""
    if pos != 0:
        pos = "transversal"
    else:
        if (a*u[0] + b*u[1] + c*u[2] + d) == 0:
            pos = "contida"
        else:
            pos = "paralela"
    return pos

def Distancia(a, b, c, d, A,B, pos):
    if pos == "transversal":
        print("Como e transversal, a distancia sera:")
        return 0
    elif pos == "contida":
        print("Como e contida, a distancia sera:")
        return 0
    elif pos == "paralela":
        distancia1 =0.0
        distancia2 = 0.0
        distancia1 = (abs(a*A[0] + b*A[1] + c*A[2] +d))/(sqrt(pow(a,2) + pow(b,2) +pow(c,2)))
        distancia2 = (abs(a*B[0] + b*B[1] + c*B[2] +d))/(sqrt(pow(a,2) + pow(b,2) +pow(c,2)))
        print("Como e paralela, as distancias do ponto A e B serao:")
        distancia = str(distancia1) + " e " + str(distancia2)
        return distancia

def opcao():
    print("")
    print("Qual opcao voce deseja?")
    print("1 - Posicao Relativa")
    print("2 - Distancia")
    print("3 - Grafico")


def calculos(u, n, a, b, c, d, A, B):
    while 1:
        opcao()
        op = int(input("Digite a opcao "))

        if op == 3:
            Grafico(A,B,n,d)

        elif op == 1:
            pos = (u[0]*n[0] + u[1]*n[1] + u[2]*n[2])

            posicao = Posicao(a, b, c, d,u, pos)
            print("Posicao relativa: ", posicao)
            print("")

        elif op == 2:
            pos = (u[0]*n[0] + u[1]*n[1] + u[2]*n[2])

            posicao = Posicao(a, b, c, d,u, pos)
            distancia = Distancia(a, b, c, d, A,B, posicao)
            print("Distancia do Pontos: ", distancia)
            print("")

        else:
            print("Opcao invalida")
            break

def Main():
    print("Qual opcao voce deseja?")
    print("1 - Utilizar o RA")
    print("2 - Pontos de reta personalizados")
    ope = int(input("Digite a opcao "))
    
    if ope == 1:
        RA = input("Digite o RA: (xxxxxxxx-x): ")

        A = [int(RA[0]), int(RA[1]),int(RA[2])]
        B = [int(RA[3]), int(RA[4]),int(RA[5])]
        C = [int(RA[6]), int(RA[7]),int(RA[9])]

        u = [int(RA[3]) - int(RA[0]), int(RA[4]) - int(RA[1]),int(RA[5]) - int(RA[2])] # b-a

        print("A reta obtida e: ", A, " + t ", u , "\n")
        print("Equacao Vetorial:")
        print("X = ",A[0],"+ (", u[0],")t")
        print("Y = ",A[1],"+ (", u[1],")t")
        print("Z = ",A[2],"+ (", u[2],")t")
        print("")

        a = int(input("Digite o a da equacao do plano: "))
        b = int(input("Digite o b da equacao do plano: "))
        c = int(input("Digite o c da equacao do plano: "))
        d = int(input("Digite o d da equacao do plano: "))

        n = [a,b,c]
        print("A equacao obtida e: ",a, "x + ", b, "y + ", c, "z + ", d ,"\n")
        print("Vetor N obtido: ", n)
        print("")

        calculos(u, n, a, b, c, d, A, B)
    
    elif ope == 2:
        x1 = int(input("Digite o x do Ponto 1: "))
        y1 = int(input("Digite o y do Ponto 1: "))
        z1 = int(input("Digite o z do Ponto 1: "))
        A = [x1, y1,z1]


        x2 = int(input("Digite o x do Ponto 2: "))
        y2 = int(input("Digite o y do Ponto 2: "))
        z2 = int(input("Digite o z do Ponto 2: "))
        B = [x2, y2,z2]


        u = [int(B[0]) - int(A[0]), int(B[1]) - int(A[1]),int(B[2]) - int(A[2])] # b-a

        print("A reta obtida e: ", A, " + t ", u , "\n")
        print("Equacao Vetorial:")
        print("X = ",A[0],"+ (", u[0],")t")
        print("Y = ",A[1],"+ (", u[1],")t")
        print("Z = ",A[2],"+ (", u[2],")t")
        print("")

        a = int(input("Digite o a da equacao do plano: "))
        b = int(input("Digite o b da equacao do plano: "))
        c = int(input("Digite o c da equacao do plano: "))
        d = int(input("Digite o d da equacao do plano: "))

        n = [a,b,c]
        print("A equacao obtida e: ",a, "x + ", b, "y + ", c, "z + ", d ,"\n")
        print("Vetor N obtido: ", n)
        print("")

        calculos(u, n, a, b, c, d, A, B)
    else:
        print("Opcao invalida")
Main()
