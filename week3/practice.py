import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1, 4))
array3 = np.zeros((2, 5))

print(array1[0], array1[2])
print(array2[0][0], array2[0][3])
print(array3[1][0], array3[1][3])
print(array1[0][0]) # Index Error
