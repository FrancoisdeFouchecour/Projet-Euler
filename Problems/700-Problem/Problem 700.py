import time 
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import bezout

problem_number = 700
problem_input = 1504170715041707
problem_input_modulo = 4503599627370517


#Solution


def solution(K, modulo):
    sumation = K 
    
    Eulercoin, periode = K, modulo
       
    while Eulercoin !=0:
        periode = periode%Eulercoin 
        
        while Eulercoin >= periode:
            Eulercoin -= periode
            sumation += Eulercoin

    return sumation

    
#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(problem_input, problem_input_modulo)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"
string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
