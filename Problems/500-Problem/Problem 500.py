import time 
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import sieve_for_primes_to


problem_number = 500
test_input = 4
test_solution = 120
problem_input = 5


def min_index(Set):
    value = np.infty
    index = -1
    for i in range(len(Set)):
        if Set[i] < value:
            value = Set[i]
            index = i
    return index
    
    
#Solution


def solution(limit):
    MODULUS = 500500507
    primes = sieve_for_primes_to(7376508) #to have 500500 primes
    exp_tab = [1 for _ in range(len(primes))]

    index_begin = 0
    index_end = len(primes) - 1
    while index_begin < index_end:
        while primes[index_begin]**(exp_tab[index_begin] + 1) < primes[index_end]:
            exp_tab[index_begin] = 2*(exp_tab[index_begin] + 1) - 1
            exp_tab[index_end] = 0
            index_end -= 1
        index_begin += 1
            
    result = 1
    for i in range(len(primes)):
        result *= primes[i]**exp_tab[i]
        result = result%MODULUS
    
    return result


#Test & Result



begin_test = time.time()
test_value = solution(test_input)
end_test = time.time()
test_time = end_test - begin_test


begin_problem = time.time()
problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""
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
string += "\n\n\nRESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
