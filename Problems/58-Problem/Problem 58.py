import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime


problem_number = 58
problem_input = 0.1


def south_east(n):
    return(4*n**2 - 2*n +1)

def south_west(n):
    return(4*n**2 + 1)

def north_west(n):
    return(4*n**2 + 2 * n + 1)

def north_east(n):
    return(4*n**2 + 4 * n + 1)



#Solution


def solution(limit):
    n = 1
    nb_prime = 3
    nb_total = 5
    
    while nb_prime/nb_total > limit:
        n += 1
        if is_prime(south_east(n)) == south_east(n):
            nb_prime += 1
        if is_prime(south_west(n)) == south_west(n):
            nb_prime += 1
        if is_prime(north_east(n)) == north_east(n):
            nb_prime += 1
        if is_prime(north_west(n)) == north_west(n):
            nb_prime += 1
        nb_total += 4
        
    return (2*n +1)
    

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
