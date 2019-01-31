import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime


problem_number = 35
test_input = 100
test_solution = 13 
problem_input = 1000000


#Solution


def solution(limit):
    result = []
    prime_list = [n for n in range(2, limit) if is_prime(n) == n]
    
    for prime in prime_list:
        string_prime = str(prime)
        prime_count = 0
        for i in range(len(string_prime) - 1):
            string_prime = string_prime[-1]+string_prime[0:-1]
            if int(string_prime) == is_prime(int(string_prime)):
                prime_count += 1
        if prime_count == len(string_prime) - 1:
            result.append(prime)
            
    return len(result)


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
