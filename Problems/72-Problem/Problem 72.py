import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import min_factor


problem_number = 72
test_input = 8
test_solution = 21
problem_input = 1000000


def solution(limit):
    primes = min_factor(limit)
    phi_tab = [0 for _ in range(limit + 1)]
    
    for n in range(2, limit + 1):
        k = primes[n]
        if k == n:
            phi_tab[n] = n - 1
        elif n%(k*k) == 0:
            phi_tab[n] = k*phi_tab[n//k]
        else:
            phi_tab[n] = (k - 1)*phi_tab[n//k]
        
    return sum(phi_tab)


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value = solution(test_input)
end_test = time.time()
test_time = end_test - begin_test

string += "TEST #1\n\n"
string += "Input: "+str(test_input)+"\n"
string += "Output: "+str(test_value)+"\n"
string += "Answer: "+str(test_solution)+"\n"
string += "Computation time: "+str(test_time)+" sec\n"
string += "Verification: "

if(test_value == test_solution):
    string += "TRUE"
else:
    string += "FALSE"
    

begin_problem = time.time()
problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "\n\n\nRESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
