import numpy as np
from scipy import integrate
def test_function(x):
    answer = np.log2(x+1)
    return answer
def estimate(N):
    randomly_generated_array = np.random.uniform(0, 1, N)
    #print(randomly_generated_array)
    answer_mat = test_function(randomly_generated_array)
    #print(answer_mat)
    sum = 0
    for i in answer_mat:
        sum = sum + i
    estimation = sum * 1.000 / N
    print("Estimation:", estimation)
    print("Error is approximate to:", estimation-0.5573)
    #真实值(2ln(2)-1)/ln(2) approx 0.5573

estimate(5000)