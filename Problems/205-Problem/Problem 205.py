import time 
import numpy as np


problem_number = 205
        

#Solution


def solution():
    C = [0 for i in range(37)]
    P = [0 for i in range(37)]
    
    for dice_1 in range(1, 7):
        for dice_2 in range(1, 7):
            for dice_3 in range(1, 7):
                for dice_4 in range(1, 7):
                    for dice_5 in range(1, 7):
                        for dice_6 in range(1, 7):
                            C[dice_1 + dice_2 + dice_3 + dice_4 + dice_5 + dice_6] += 1
    
    for i in range(37):
        C[i] = C[i]/46656

    for dice_1 in range(1, 5):
        for dice_2 in range(1, 5):
            for dice_3 in range(1, 5):
                for dice_4 in range(1, 5):
                    for dice_5 in range(1, 5):
                        for dice_6 in range(1, 5):
                            for dice_7 in range(1, 5):
                                for dice_8 in range(1, 5):
                                    for dice_9 in range(1, 5):
                                        P[dice_1 + dice_2 + dice_3 + dice_4 + dice_5 + dice_6 + dice_7 + dice_8 + dice_9] += 1
    
    for i in range(37):
        P[i] = P[i]/262144
    
    probability = 0
    
    for c in range(37):
        probability += sum(P[c + 1:])*C[c]
        
    return np.ceil(probability*10**7)/10**7


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
