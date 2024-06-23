import numpy as np
import matplotlib

rng = np.random.default_rng()

def Spacer():
    print('\n___________________________________________\n')

def NewLine():
    print('\n')


Spacer()

a_2d = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 10, 11, 12], 
                 [1, 2, 3, 4]])

unique_values, indices_list, occurrence_count = np.unique(a_2d, axis=1, return_index=True, return_counts=True)
#print(indices_list)
print(unique_values)
#print(occurrence_count)

help(print)
