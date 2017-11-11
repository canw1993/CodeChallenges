# Author: Can Wang, Bowen Deng
# Generate a random Fibonacci number smaller than equal to n (n>0) in O(log(n)) time

import math
import random

def matrix_power(mat, n):
    # compute mat^n, mat is a square matrix
    N = len(mat)
    if n == 0:
        zeros = [[0. for _ in range(N)] for _ in range(N)]
        for i in range(N):
            zeros[i][i] = 1.
        return zeros
    else:
        # compute mat^{[n/2]}
        sub_result = matrix_power(mat, int(n/2))
        # multiply sub_result
        result = [[0. for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += sub_result[i][k] * sub_result[k][j]
        # if n is odd, multiply sub_result by mat
        if n%2 == 0:
            return result
        rtn = [[0. for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    rtn[i][j] += result[i][k] * mat[k][j]
        return rtn
        
def fib(n):
    # give the n-the fibonacci number
    mat_pow = matrix_power([[0,1],[1,1]], n)
    return mat_pow[0][1]
    
def GiveRandFibNum(n):
    while True:
        if n > 2:
            m = random.randint(1, min(n, 10+int(5*math.log2(n*5))))
            fib_m = fib(m)
            if fib_m <= n:
                return fib_m
        else:
            return 1
            
print(GiveRandFibNum(6))
    
