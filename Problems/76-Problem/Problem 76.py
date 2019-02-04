import time 


problem_number = 76
test_input = 5
test_solution = 6
problem_input = 100


#Solution


def solution(limit):
    matrix_value = [[0 for i in range(limit)] for i in range(limit)]
    
    for i in range(limit):
        matrix_value[i][0] = 1
        matrix_value[i][i] = 1

    for n in range(2, limit):
        for k in range(1, n):
            matrix_value[n][k] = matrix_value[n - 1][k - 1] + matrix_value[n - k - 1][k]
            
    return(sum(matrix_value[-1]) - 1)


#Test & Result


begin_test = time.time()
test_value = solution(test_input)
end_test = time.time()
test_time = end_test - begin_test


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

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
