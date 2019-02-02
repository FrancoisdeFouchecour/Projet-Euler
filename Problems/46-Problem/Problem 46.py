import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime


problem_number = 46
    

#Solution


def solution():
    n = 3
    double_square = [2]
    next_square = 2
    b = True
    while b :
        n += 2
        if n > 2 * next_square**2:
            double_square.append(2 * next_square**2)
            next_square += 1
        
        if is_prime(n) != n:
            b = False
            for square in double_square:
                if is_prime(n - square) == n - square:
                    b = True
                    break
    return n


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
 