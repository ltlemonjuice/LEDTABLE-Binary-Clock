'''
Reads continuosly save.matrix file in current directory and displays the matrix wiht correct RGB values, just like the LEDTABLE itself.


save.matrix has to be present!

'''



import numpy as np
import time
import matplotlib.pyplot as plt

matrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]
cmatrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]
matrix = np.flipud(np.rot90(matrix))


def adjustVal():
    cmatrix = matrix
    for x in range(0, 10):
        for y in range(0, 10):
            for i in range(0, 3):
                cmatrix[x][y][i] /= float(255)





adjustVal()
arr = plt.imshow(cmatrix, interpolation="nearest")
plt.axis("off")



while True:
    try:
        f = open("save.matrix")
        matrix = eval(f.read())
    except:
        pass
    adjustVal()
    arr.set_data(matrix)
    plt.pause(0.05)
