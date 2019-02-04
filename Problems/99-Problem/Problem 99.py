import time 
import numpy as np


problem_number = 99


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()

problem_list = raw_data.split("\n")
for i in range(len(problem_list)):
    problem_list[i] = problem_list[i].split(',')
    problem_list[i][0] = int(problem_list[i][0])
    problem_list[i][1] = int(problem_list[i][1])


#Solution


def solution(input_list):
    highest_log_value = 0
    higest_row = 0
    for problem in input_list:
        if problem[1] * np.log(problem[0]) > highest_log_value:
            higest_row = input_list.index(problem) + 1
            highest_log_value = problem[1] * np.log(problem[0])
    return higest_row


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(problem_list)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
