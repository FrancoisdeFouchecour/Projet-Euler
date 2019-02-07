import time
from scipy.optimize import linear_sum_assignment
 

problem_number = 345
test_solution = 3315


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()


matrix_problem = []
for row in raw_data.split('\n'):
    matrix_problem.append(row.split(' '))

for i in range(len(matrix_problem)):
    for j in range(len(matrix_problem[0])):
        matrix_problem[i][j] = int(matrix_problem[i][j])


#Solution


def solution(matrix_input):
    size = len(matrix_input)
    max_matrix = max([max(row) for row in matrix_input])
    
    min_matrix = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            min_matrix[i][j] = max_matrix - matrix_input[i][j]
    
    row_ind, col_ind = linear_sum_assignment(min_matrix)
    return sum([matrix_input[row_ind[i]][col_ind[i]] for i in range(size)])


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value = solution([[7, 53, 183, 439, 863], [497, 383, 563, 79, 973], [287, 63, 343, 169, 583], [627, 343, 773, 959, 943], [767, 473, 103, 699, 303]])
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
problem_value = solution(matrix_problem)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "\n\n\nRESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
