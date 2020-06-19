from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 

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