import time 
import numpy as np


problem_number = 45


def is_pentagonal(x):
    d = int(np.sqrt(24 * x + 1))
    return (d * d == 24 * x + 1 and (1 + d)%6 ==0)
    

#Solution


def solution():
    n = 2
    T = 6
    while not(n%2 == 1 and is_pentagonal(T) and n != 285):
        n += 1
        T = n*(n+1)//2
    
    return T


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
 