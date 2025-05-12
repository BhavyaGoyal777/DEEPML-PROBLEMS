import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    trace = 0
    
    for i,j in enumerate(matrix):
        trace += j[i]
    
    array = np.array(matrix)
    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    eigenValueOne = (trace + np.sqrt((trace**2)-(4*1*det))) / (2) 
    eigenValueTwo = (trace - np.sqrt((trace**2)-(4*1*det)))  / (2)
    

	return [eigenValueOne,eigenValueTwo]
