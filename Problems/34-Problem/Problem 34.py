import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import factorial


problem_number = 34


#Solution


def solution():
    result = 0
    fact_tab = [factorial(i) for i in range(10)]
    for num in range(3, 1000000):
        digit_sum = 0
        for char in str(num):
            digit_sum += fact_tab[int(char)]
        if digit_sum == num:
            result += num            
    return result

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
