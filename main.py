from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 

#pip install numpy
#pip install -U Pillow
#pip install matplotlib && pip install --upgrade matplotlib

import calculator

def main():

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
    calculator.calculos(u, n, a, b, c, d, A, B)


if __name__ == "__main__":
    main()
