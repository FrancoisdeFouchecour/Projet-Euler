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


def solutionHaut(K, modulo):
    Eulercoin = K
    Euler_index = 1
    Euler_count = 1
    
    sequence_n = K
    index = 1
    
    sumation = K 
    
    while Eulercoin > 1 and Eulercoin > 10**8:
        index += 1
        sequence_n += K
        sequence_n = sequence_n%modulo
    
        if sequence_n < Eulercoin:
            Eulercoin = sequence_n
            Euler_index = index
            Euler_count += 1
            sumation += Eulercoin
            print(Euler_count, Eulercoin)
    
    return sumation


def solutionBas(K, modulo):
    r, u, n0 = bezout(modulo, K)
    n0 = n0%modulo
    
    Eulercoin_index = n0
    n = n0
    u_n = 1
    
    sumation = 1
    
    while n > 1 :
        u_n += 1
        n = (n + n0)%modulo
        
        if n < Eulercoin_index:
            Eulercoin_index = n
            if Eulercoin_index < 10**8:
                break
            sumation += u_n
            print(Eulercoin_index, u_n, sumation)
        
    return sumation
    
#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solutionHaut(problem_input, problem_input_modulo) + solutionBas(problem_input, problem_input_modulo)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"
string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
