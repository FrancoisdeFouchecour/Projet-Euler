import time 
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import min_factor
from algorithm import is_permutation

problem_number = 70
problem_input = 10000000


#Solution


def solution(limit):
    primes = min_factor(limit - 1)
    phi_tab = [0 for _ in range(limit)]
    
    phi_tab[1] = 1
    for n in range(2, limit):
        k = primes[n]
        if k == n:
            phi_tab[n] = n - 1
        elif n%(k*k) == 0:
            phi_tab[n] = k*phi_tab[n//k]
        else:
            phi_tab[n] = (k - 1)*phi_tab[n//k]
    
    
    min_value = np.infty
    min_index = -1
    
    for n in range(2, limit):
        if n/phi_tab[n] < min_value and is_permutation(str(n), str(phi_tab[n])):
            min_value = n/phi_tab[n]
            min_index = n
    
    return min_index


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""
    

begin_problem = time.time()
problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
