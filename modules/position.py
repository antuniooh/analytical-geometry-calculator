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