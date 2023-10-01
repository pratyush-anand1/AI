import numpy as np

def normalize_2d(matrix):
    norm = np.linalg.norm(matrix)
    matrix = matrix/norm # normalized matrix
    return matrix

array = np.arange(-2,14,1)   # gives an array starting from -2 and ending at 13
print(array)

#converts 1d array to a matrix
matrix = array.reshape(4, 4)
print("Simple Matrix \n", matrix)
normalized_matrix = normalize_2d(matrix)
print("\nSimple Matrix \n", normalized_matrix)
max=array.max()
min=array.min()
print(max)
print(min)
normalized_matrix=(array-min)/(max-min)
print(normalized_matrix)