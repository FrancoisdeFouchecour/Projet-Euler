import time 
import numpy as np


problem_number = 700
problem_input = 1504170715041707
problem_input_modulo = 4503599627370517


#Solution


def solution(n, modulo):
    Eulercoin = n
    Euler_index = 1
    Euler_count = 1
    
    sequence_n = n
    index = 1
    periode_trouve = 0
    
    sumation = n 
    
    while True:
        index += 1
        sequence_n += n
        sequence_n = sequence_n%modulo
        
        if sequence_n < Eulercoin:
            periode_trouve = index - Euler_index
            Eulercoin = sequence_n
            Euler_index = index
            Euler_count += 1
            print(Euler_count, Eulercoin, Euler_index)
            
            if periode_trouve != 0:
                print("Periode trouve :"+str(periode_trouve))
                while (sequence_n + periode_trouve*n)%modulo < Eulercoin:
                    index += periode_trouve
                    sequence_n = sequence_n + n*periode_trouve
                    sequence_n = sequence_n%modulo
                    Eulercoin = sequence_n
                    Euler_index = index
                    Euler_count += 1
                    print("MERCI PERIODE")
                    print(Euler_count, Eulercoin, Euler_index)
                    
                print("Periode perdue :"+str(periode_trouve)+"\n")
                periode_trouve = 0
                index += periode_trouve
    return 0
    

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
