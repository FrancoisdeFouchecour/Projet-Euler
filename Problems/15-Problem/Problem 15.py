import time 


problem_number = 15
test_input = 2
test_solution = 6
problem_input = 20


#Solution


def solution(limit):
    matrix_path = [[0 for j in range(limit + 1)] for i in range(limit + 1)]
    matrix_path[0] = [1 for j in range(limit + 1)]
    
    for i in range(1, limit +1 ):
        for j in range(limit + 1):
            matrix_path[i][j] = matrix_path[i][j - 1] + matrix_path[i - 1][j]
        
    return matrix_path[limit][limit]


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