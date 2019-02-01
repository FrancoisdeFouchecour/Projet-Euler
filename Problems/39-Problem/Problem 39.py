import time 
import numpy as np

problem_number = 39
problem_input = 1000

#Solution


def solution(limit):
    max_triangle = 0
    max_p = 0
    for p in range(4, limit + 1):
        triangle_count = 0
        for a in range(1, p//3):
            for b in range(a, (p - a)//2):
                c = p - a - b
                if a*a + b*b == c*c:
                    triangle_count += 1
        if triangle_count > max_triangle:
            max_triangle = triangle_count
            max_p = p
            
    return max_p

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
