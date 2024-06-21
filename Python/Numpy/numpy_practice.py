import numpy as np

def Spacer():
    print('\n___________________________________________\n')

def NewLine():
    print('\n')



a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

five_up = (a > 5) | (a == 5)


print(a[five_up])