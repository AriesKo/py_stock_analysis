import numpy as np

if __name__ == "__main__":
    A = np.array([[1,2,3],[4,5,6]])
    print(A)
    print(A.shape)
    print(A.ndim)
    print(A.dtype)
    print(A.itemsize)
    print(A.size)
    print(type(A))
    print(A.max(), A.mean(), A.min(), A.sum())
    
    A_f = A.flatten()
    print(A_f)
