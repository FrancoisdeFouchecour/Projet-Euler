import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import prime_decomposition

problem_number = 26
test_input = 10
test_solution = 7
problem_input = 1000


#Solution


def solution(limit):
    max_decimal = 0
    max_d = 0
    
    for d in range(2, limit):
        decomposition = prime_decomposition(d)
        if decomposition.count(2) + decomposition.count(5) != len(decomposition):
            exp_maj = 1
            exp_min = 0
            while (10**exp_maj - 10**exp_min)%d != 0:
                if exp_min + 1 == exp_maj:
                    exp_maj += 1
                    exp_min = 0
                else:
                    exp_min += 1
            if exp_maj - exp_min > max_decimal:
                max_decimal = exp_maj - exp_min
                max_d = d
    
    return max_d

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