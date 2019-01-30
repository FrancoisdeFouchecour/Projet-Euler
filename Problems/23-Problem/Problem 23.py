import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import sum_of_divisors
from algorithm import two_sum


problem_number = 23


#Solution


def solution():
    result = 0
    list_abundant = []
    
    for num in range(10, 28123):
        if sum_of_divisors(num) - num > num:
            list_abundant.append(num)
            
    for num in range(1, 28124):
        if not two_sum(list_abundant, num) and not(num%2 == 0 and list_abundant.count(num/2) > 0):
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
