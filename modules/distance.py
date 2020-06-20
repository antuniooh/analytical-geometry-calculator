from math import *

def Distancia(a, b, c, d, A,B, pos):
    if pos == "transversal":
        return("Como e transversal, a distancia sera: 0")
    elif pos == "contida":
        return("Como e contida, a distancia sera: 0")
    elif pos == "paralela":
        distancia1 =0.0
        distancia2 = 0.0
        distancia1 = (abs(a*A[0] + b*A[1] + c*A[2] +d))/(sqrt(pow(a,2) + pow(b,2) +pow(c,2)))
        distancia2 = (abs(a*B[0] + b*B[1] + c*B[2] +d))/(sqrt(pow(a,2) + pow(b,2) +pow(c,2)))
        distancia = ("Como e paralela, as distancias do ponto A e B serao:\n")  + str(distancia1) + " e " + str(distancia2)
        return distancia