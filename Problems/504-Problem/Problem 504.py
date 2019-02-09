import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import gcd
from algorithm import quick_search


problem_number = 504
test_input = 4
test_solution = 42
problem_input = 100


def triangle(a, b):
    return ((a+1)*(b+1) - gcd(a, b) - 1)//2 - a - b + 1


def quadri(a, b, c, d): 
    return triangle(a, b) + triangle(b, c) + triangle(c, d) + triangle(d, a) + a + b + c + d - 3


#Solution


def solution(limit):
    squares = [i*i for i in range(int(1 + limit*2**0.5))]
    result = 0
    for a in range(1, limit + 1):
        print(a)
        for b in range(1, limit + 1):
            for c in range(1, limit + 1):
                for d in range(1, limit + 1):
                    if quick_search(squares, quadri(a, b, c, d)):
                        result += 1
    
    return result


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
