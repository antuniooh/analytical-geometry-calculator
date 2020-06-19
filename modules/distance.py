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