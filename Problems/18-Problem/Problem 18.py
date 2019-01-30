import time 

problem_number = 18
test_solution = 23


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()

size = raw_data.count("\n")
matrix_value = [[0 for j in range(size)] for i in range(size)]
index_ver = 0
index_hor = 0

for index in range(len(raw_data)):
    if index%3 == 1:
        matrix_value[index_ver][index_hor] += int(raw_data[index - 1:index + 1])
    if index%3 == 2:
        if raw_data[index] == "\n":
            index_ver += 1
            index_hor = 0
        elif raw_data[index] == " ":
            index_hor += 1


#Solution


def solution(matrix_input):
    size = len(matrix_input)
    matrix_result = [[0 for j in range(size)] for i in range(size)]
    
    #first colllum
    matrix_result[0][0] = matrix_input[0][0]
    for i in range(1, size):
        matrix_result[i][0] = matrix_result[i - 1][0] + matrix_input[i][0]
    
    for i in range(1, size):
        for j in range(1, i + 1):
            matrix_result[i][j] += max(matrix_result[i - 1][j], matrix_result[i - 1][j - 1])
            matrix_result[i][j] += matrix_input[i][j]
            
    return max(matrix_result[size - 1])


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value = solution([[3, 0, 0, 0], [7, 4, 0, 0], [2, 4, 6, 0], [8, 5, 9, 3]])
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