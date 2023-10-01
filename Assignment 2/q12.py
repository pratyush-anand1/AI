import numpy as np

#https://pylessons.com/Logistic-Regression-part3

l1 = np.array([9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0])
l2 = np.array([9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0])

dotProduct = l1.dot(l2)
print("Dot Product:",dotProduct)

outerProuduct = np.outer(l1,l2)
print("Outer Product: \n",outerProuduct)

multiply = l1*l2
print(multiply)