import time 
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from algorithm import quick_search, quick_add


problem_number = 346
test_input = 1000
test_solution = 15864
problem_input = 10**12


#Solution


def solution(limit):
    b = 2
    result = [1]
    while 3 <= np.log(limit*(b - 1) + 1)/np.log(b):
        for n in range(3,  int(np.log(limit*(b - 1) + 1)/np.log(b)) + 1) :
            x = (b**n -1)//(b - 1)
            if not(quick_search(result, x)):
                result.insert(quick_add(result, x), x)
        b += 1
    
    return sum(result)


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
