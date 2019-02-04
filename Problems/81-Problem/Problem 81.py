import time 


problem_number = 81
test_solution = 2427


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
    
    max_matrix = [[0 for j in range(size)] for i in range(size)]
    max_matrix[0][0] = matrix_input[0][0]    
    for i in range(1, size):
        max_matrix[i][0] = max_matrix[i - 1][0] + matrix_input[i][0]
        max_matrix[0][i] = max_matrix[0][i - 1] + matrix_input[0][i]
    
    for i in range(1, size):
        for j in range(1, size):
            max_matrix[i][j] = matrix_input[i][j] + min(max_matrix[i][j - 1], max_matrix[i - 1][j])
    
    return max_matrix[-1][-1]


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value = solution([[131, 673, 234, 703, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]])
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
