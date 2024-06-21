import numpy as np

'''
https://numpy.org/doc/2.0/user/absolute_beginners.html
'''

def Spacer():
    print('\n___________________________________________\n')

def NewLine():
    print('\n')


a = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]])


Spacer()

print('array is:', a)

Spacer()

#The number of dimensions of an array is contained in the ndim attribute. also known as the axis / axes
print('number of dimensions, or axis/axes: ', a.ndim)

Spacer()

#The shape of an array is a tuple of non-negative integers that specify the number of elements along each dimension.
print('array shape:', a.shape)

Spacer()

#The fixed, total number of elements in array is contained in the size attribute.
print('total number of elements: ' , a.size)

Spacer()
###############################_______________________________________###############################
#HOW TO CREATE A BASIC ARRAY
print('HOW TO CREATE A BASIC ARRAY \n')

print('array filled with 0s: ')
#array filled with 0's
print(np.zeros(5))
print('\n')
print('array filled with 1s: ')
#array filled with 1's
print(np.ones(5))
print('\n')
print('Empty array: ')
print(np.empty(5))

Spacer()

#You can create an array with a range of elements:
print('array with a range of elements: ', np.arange(4))
NewLine()

#array that contains a range of evenly spaced intervals.Parameters are the first number, last number, and the step size.
print('spaced interval range: ', np.arange(10, 110, 10))
NewLine()
#use np.linspace() to create an array with values that are spaced linearly in a specified interval: first number, last number, num=enter interval num
print('spaced interval range: ', np.linspace(10, 10000, num=10))