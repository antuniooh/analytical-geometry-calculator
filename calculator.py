import os

from modules import graph
from modules import position
from modules import option
from modules import distance

def calculos(u, n, a, b, c, d, A, B):
    while 1:
        option.opcao()
        op = int(input("Digite a opcao "))

        if op == 3:
            graph.Grafico(A,B,n,d)

        elif op == 1:
            pos = (u[0]*n[0] + u[1]*n[1] + u[2]*n[2])

            posicao = position.Posicao(a, b, c, d,u, pos)
            print("Posicao relativa: ", posicao)
            print("")

        elif op == 2:
            pos = (u[0]*n[0] + u[1]*n[1] + u[2]*n[2])

            posicao = position.Posicao(a, b, c, d,u, pos)
            distancia = distance.Distancia(a, b, c, d, A,B, posicao)
            print("Distancia do Pontos: ", distancia)
            print("")

        else:
            print("Opcao invalida")
            break