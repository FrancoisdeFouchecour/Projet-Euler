import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import sieve_for_primes_to


problem_number = 381
test_input = 100
test_solution = 480
problem_input = 100000000


#Solution


def solution(limit):
    primes = sieve_for_primes_to(limit)
    primes.remove(2)
    primes.remove(3)
    result = 0
    
    for p in primes:
        p_minus_3 = (p - 1)//2
        
        p_minus_4 = 0
        if p%3 == 1:
            p_minus_4 = -(p_minus_3//3 - (p_minus_3%3)*(p - 1)//3)%p
        elif p%3 == 2:
            p_minus_4 = -(p_minus_3//3 + (p_minus_3%3)*(p + 1)//3)%p
            
        p_minus_5 = 0
        if p%4 == 1:
            p_minus_5 = -(p_minus_4//4 + -(p_minus_4%4)*(p - 1)//4)%p
        elif p%4 == 3:
            p_minus_5 = -(p_minus_4//4 + (p_minus_4%4)*((p + 1)//4))%p        
        
        result += (p_minus_3+ p_minus_4+ p_minus_5)%p
                
    return result
    

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
