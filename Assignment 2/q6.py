import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

n = 100
x = np.linspace(-5,5)
mu = 0
sigma = 1

y =  norm.pdf(x,mu,sigma)
print(y)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Probability Distribution function for Normal Distribution')
#plt.show()