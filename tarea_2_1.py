Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Forma 1
>>> mis_valores = [5, 6, 10, 13, 3, 4]
>>> promedio=sum(mis_valores)/len(mis_valores)
>>> promedio
6.833333333333333
>>> #Forma 2
>>> import numpy
>>> numpy.mean(mis_valores)
6.833333333333333
>>> 
