import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import prime_decomposition, prime_decomposition_normalise


problem_number = 47
test_input_1 = 2
test_solution_1 = 14
test_input_2 = 3
test_solution_2 = 644
problem_input = 4


#Solution


def solution(target):
    n = 1
    consecutive = 0
    distinct_prime = []
    while consecutive < target:
        n +=1
        decompo = prime_decomposition_normalise(prime_decomposition(n))
        nb_factor = 0
        for div, exp in decompo:
            nb_factor += 1
            if not(div in distinct_prime):
                distinct_prime.append(div)
        
        if nb_factor >= target and len(distinct_prime) >= target * consecutive:
            consecutive += 1
        else:
            consecutive = 0
            distinct_prime = []
            
    return n - consecutive + 1


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value_1 = solution(test_input_1)
end_test = time.time()
test_time = end_test - begin_test

string += "TEST #1\n\n"
string += "Input: "+str(test_input_1)+"\n"
string += "Output: "+str(test_value_1)+"\n"
string += "Answer: "+str(test_solution_1)+"\n"
string += "Computation time: "+str(test_time)+" sec\n"
string += "Verification: "

if(test_value_1 == test_solution_1):
    string += "TRUE"
else:
    string += "FALSE"
    

begin_test = time.time()
test_value_2 = solution(test_input_2)
end_test = time.time()
test_time = end_test - begin_test

string += "\n\nTEST #2\n\n"
string += "Input: "+str(test_input_2)+"\n"
string += "Output: "+str(test_value_2)+"\n"
string += "Answer: "+str(test_solution_2)+"\n"
string += "Computation time: "+str(test_time)+" sec\n"
string += "Verification: "

if(test_value_2 == test_solution_2):
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
