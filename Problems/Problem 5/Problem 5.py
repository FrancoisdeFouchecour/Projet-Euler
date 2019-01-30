import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import ppcm_multiple


problem_number = 5
test_input = 10
test_solution = 2520
problem_input = 20


#Solution


def solution(limit):
    ppcm_decomposition = ppcm_multiple([i for i in range(2,limit+1)])
    ppcm = 1
    
    for factor in ppcm_decomposition:
        ppcm *= factor
        
    return ppcm


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