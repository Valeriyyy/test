import numpy as np

a = np.array([[1,1,1],[1,2,3],[1,3,5]])
#print(a)
b = np.array([1500,3000,4500])
z = np.linalg.solve(a,b)
print(z)