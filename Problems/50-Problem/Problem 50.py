import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime


problem_number = 50
test_input_1 = 100
test_solution_1 = 41
test_input_2 = 1000
test_solution_2 = 953
problem_input = 1000000


#Solution


def solution(target):
    primes = [i for i in range(2, target) if is_prime(i) == i] 
    max_prime = 0
    max_consecutive = 1
    
    while max_consecutive < target - sum(primes[:max_consecutive]):
        max_consecutive += 1
        index = 0
        sum_prime = sum(primes[index:index + max_consecutive])
        
        if is_prime(sum_prime) == sum_prime and sum_prime < target:
            max_prime = sum_prime
        else:
            while not(is_prime(sum_prime) == sum_prime) and sum_prime < target:
                index += 1
                sum_prime = sum(primes[index:index + max_consecutive])
            if is_prime(sum_prime) == sum_prime and sum_prime < target:
                max_prime = sum_prime
                
    return max_prime


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
