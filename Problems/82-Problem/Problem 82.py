import time 
import numpy as np


problem_number = 82
test_solution = 994


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()

test = raw_data.split('\n')
matrix_value = []

for row in test:
    matrix_value.append(row.split(','))

for i in range(len(matrix_value)):
    for j in range(len(matrix_value)):
        matrix_value[i][j] = int(matrix_value[i][j])


#Solution


def solution(matrix_input):
    size = len(matrix_input)
    
    min_matrix = [[0 for j in range(size)] for i in range(size)]    
    
    for i in range(size):
        min_matrix[i][0] = matrix_input[i][0]
        
    for j in range(1, size):
        for i in range(size):
            
            min_value = np.infty
            
            for previous_index in range(size):
                
                value = min_matrix[previous_index][j - 1]
                
                if previous_index == i:
                    value += matrix_input[i][j]
                elif previous_index < i:
                    for index in range(previous_index, i + 1):
                        value += matrix_input[index][j]
                else:
                    for index in range(i, previous_index + 1):
                        value += matrix_input[index][j]
                        
                if value < min_value:
                    min_value = value
                    
            min_matrix[i][j] = min_value
    
    result = np.infty
    for i in range(size):
        if result > min_matrix[i][size - 1]:
            result = min_matrix[i][size - 1]
    
    return result


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value = solution([[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]])
end_test = time.time()
test_time = end_test - begin_test

string += "TEST #1\n\n"
string += "Output: "+str(test_value)+"\n"
string += "Answer: "+str(test_solution)+"\n"
string += "Computation time: "+str(test_time)+" sec\n"
string += "Verification: "

if(test_value == test_solution):
    string += "TRUE"
else:
    string += "FALSE"
    

begin_problem = time.time()
problem_value = solution(matrix_value)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "\n\n\nRESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
