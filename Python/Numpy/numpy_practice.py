import numpy as np

def Spacer():
    print('\n___________________________________________\n')

def NewLine():
    print('\n')



data = np.array(([1,2],
                 [3,4],
                 [5,6]))


print(data.sum(axis=0))
print(data.sum(axis=1))
