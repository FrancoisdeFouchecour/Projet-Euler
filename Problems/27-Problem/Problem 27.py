import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime

problem_number = 27
test_input = 41
test_solution = -41
problem_input = 1000


def phi(n, a, b):
    return (n * n + n * a + b)
    
    
#Solution


def solution(limit):
    max_consecutive_prime = 0
    max_consecutive_prime_a = 0
    max_consecutive_prime_b = 0
    prime_sub_lim = [n for n in range(2, limit + 1) if is_prime(n) == n]
    p_zero_possible = len(prime_sub_lim)
    prime_sub_lim += [n for n in range(limit + 1, 2 * limit + 1) if is_prime(n) == n]
    p_one_possible = len(prime_sub_lim)

    for p_zero_index in range(p_zero_possible):
        for p_one_index in range(p_one_possible):
            b = prime_sub_lim[p_zero_index]
            a = prime_sub_lim[p_one_index] - b - 1
            
            if a > - b - 1 and abs(a) < limit:
                index_count = 0
                while is_prime(phi(index_count, a, b)) == phi(index_count, a, b):
                    index_count += 1
                                   
                if index_count > max_consecutive_prime:
                    max_consecutive_prime = index_count
                    max_consecutive_prime_a = a
                    max_consecutive_prime_b = b
        
    return (max_consecutive_prime_a * max_consecutive_prime_b)

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
#◘problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "\n\n\nRESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()