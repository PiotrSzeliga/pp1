import matplotlib.pyplot as plt
import numpy as np

dictionary = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
x = dictionary.keys()
y = dictionary.values()
plt.bar(x,y)
plt.show()