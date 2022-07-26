
import numpy as np
import matplotlib.pyplot as plt



def demo(x):
    pass

if __name__ == '__main__':
    x = list(np.linspace(0.001, stop=0.99999, num=100))
    y =  [-np.log(i) for i in x]
    plt.plot(x, y)
    plt.show()

