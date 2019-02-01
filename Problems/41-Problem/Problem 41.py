import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime

problem_number = 41


def is_pandigital(string):
    digits = [i for i in range(1, len(string) + 1)]
    b = True
    for dig in digits:
        b = b and (string.count(str(dig)) == 1)         
    return b


#Solution


def solution():
    result = []
    for i in range(1, 10000000):
        if is_pandigital(str(i)) and is_prime(i) == i:
            result.append(i)
    return result[-1]

#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution()
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
