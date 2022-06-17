import numpy as np
def getsumofneighbors(matrix, i, j):
    region = matrix[max(0, i-1) : i+2,
                    max(0, j-1) : j+2]
    return np.sum(region) - matrix[i, j] # Sum the region and subtract center

m = np.array([[1,1,1]
              ,[1,1,1]
              ,[1,1,1]])

print(getsumofneighbors(m, 1, 1))