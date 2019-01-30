import time
import numpy as np

problem_number = 9
test_input = 12
test_solution = 3*4*5 
problem_input = 1000


#Solution


def is_square(number):
    sqrt = int(np.sqrt(number))
    return(sqrt*sqrt == number)    
    
    
def solution(target):
    for a in range(1,target):
        for b in range(a+1, target):
            c = a**2 + b**2
            if is_square(c) and a + b + int(np.sqrt(c)) == target:
                return(a*b*int(np.sqrt(c)))
        
    return("solution not found")


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value = solution(test_input)
end_test = time.time()
test_time = end_test - begin_test

string += "TEST #1\n\n"
string += "Input: "+str(test_input)+"\n"
string += "Output: "+str(test_value)+"\n"
string += "Answer: "+str(test_solution)+"\n"
string += "Computation time: "+str(test_time)+" sec\n"
string += "Verification: "

if(test_value == test_solution):
    string += "TRUE"
else:
    string += "FALSE"
    

begin_problem = time.time()
problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "\n\n\nRESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()