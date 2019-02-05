import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime


problem_number = 357
test_input = 100
test_solution = 401
problem_input = 100000000


#Solution


def solution(limit):
    result = 1
    for i in range(1, limit//2):
        n = 2 * i
        d = 1
        b = True
        while d*d <= n:
            if n%d == 0:
                if n%(d*d) == 0 and d != 1:
                    b = False
                    d = n
                if not(is_prime(d + n//d) == d + n//d):
                    b = False 
                    d = n
            d += 1
        
        if b:
            result += n
            
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
