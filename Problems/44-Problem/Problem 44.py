import time 
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from algorithm import two_sum_index


problem_number = 44


def is_pentagonal(x):
    d = int(np.sqrt(24 * x + 1))
    return (d * d == 24 * x + 1 and (1 + d)%6 ==0)
    

#Solution


def solution():
    pentagonal_number = []
    n = 0
    D = 0
    while D == 0: 
        n += 1
        P = int(0.5*n*(3*n-1))
        pentagonal_number.append(P)
        sum_list = two_sum_index(pentagonal_number, P)
        for couple in sum_list:
            if is_pentagonal(couple[1]-couple[0]):
                D = couple[1]-couple[0]
    return D


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""


begin_problem = time.time()
problem_value = solution()
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
 