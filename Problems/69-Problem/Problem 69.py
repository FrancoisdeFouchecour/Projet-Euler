import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import phi


problem_number = 69
test_input = 10
test_solution = 6
problem_input = 1000000


#Solution


def solution(limit):
    max_result = 2.0
    max_n = 0
    for n in range(2, limit + 1):
        result = n/phi(n)
        if result > max_result:
            max_result = result
            max_n = n
    return max_n


#Test & Result


begin_test = time.time()
test_value = solution(test_input)
end_test = time.time()
test_time = end_test - begin_test


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
