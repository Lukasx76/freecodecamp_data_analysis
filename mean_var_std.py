import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    else:
        numpy_arr = np.array(list)
        
        numpy_2darr = np.reshape(numpy_arr, (3,3))

        calculations = {
            'mean': [numpy_2darr.mean(axis=0).tolist(),numpy_2darr.mean(axis=1).tolist(), numpy_arr.mean()],
            'variance': [numpy_2darr.var(axis=0).tolist(),numpy_2darr.var(axis=1).tolist(), numpy_arr.var()],
            'standard deviation': [numpy_2darr.std(axis=0).tolist(),numpy_2darr.std(axis=1).tolist(), numpy_arr.std()],
            'max': [numpy_2darr.max(axis=0).tolist(),numpy_2darr.max(axis=1).tolist(), numpy_arr.max()],
            'min': [numpy_2darr.min(axis=0).tolist(),numpy_2darr.min(axis=1).tolist(), numpy_arr.min()],
            'sum' : [numpy_2darr.sum(axis=0).tolist(),numpy_2darr.sum(axis=1).tolist(), numpy_arr.sum()]
            }
        return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))
