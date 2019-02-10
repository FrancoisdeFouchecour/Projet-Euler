import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import new_decmpo


problem_number = 622
test_input = 8
test_solution = 412
problem_input = 60


def s(n):
    #n is even > 4
    exp = 1
    r = 2
    while r != 1:
        r *= 2
        r = r%(n - 1)
        exp += 1
    return exp
    

#Solution


def solution(limit):
    result = []
    
    decompo = new_decmpo(2**limit - 1)
    divisor = [decompo[0][0]**i for i in range(0, decompo[0][1] + 1)]
    
    for i in range(1, len(decompo)):
        new_divisor = []
        for div in divisor:
            new_divisor += [div*decompo[i][0]**j for j in range(0, decompo[i][1] + 1)]
        divisor = new_divisor
    
    divisor.remove(1)
    for d in divisor:
        if s(d + 1) == limit:
            result.append(d + 1)
    
    return sum(result)


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
