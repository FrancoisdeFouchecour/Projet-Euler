import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime


problem_number = 37
problem_input = 11


#Solution


def solution(limit):
    result = []
    prime_left= [prime for prime in range(2, 10) if is_prime(prime) == prime]
    prime_right= [prime for prime in range(2, 10) if is_prime(prime) == prime]
    
    size_index = 1
    
    while len(result) < limit:
        new_prime_left = []
        new_prime_right = []
        
        for prime in prime_left:
            for i in range(1, 10):
                new_num = i + prime * 10
                if is_prime(new_num) == new_num:
                    new_prime_left.append(new_num)
        
        for prime in prime_right:
            for i in range(1, 10):
                new_num = i*10**size_index + prime
                if is_prime(new_num) == new_num:
                    new_prime_right.append(new_num)
        
        prime_left = new_prime_left
        prime_right = new_prime_right
        
        for prime in prime_left:
            if prime in prime_right:
                result.append(prime)
                                
        size_index += 1
    
    return sum(result)

#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
