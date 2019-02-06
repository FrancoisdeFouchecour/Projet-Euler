import time 


problem_number = 85
problem_input = 2000000

    
#Solution


def solution(limit):
    max_row = int(limit**0.3)
    matrix_value = [[0 for j in range(max_row + 1)] for i in range(max_row + 1)]

    for n in range(1, max_row + 1):
        matrix_value[n][1] = n*(n+1)//2
    
    for n in range(2, max_row + 1):
        for p in range(2, n + 1):
            matrix_value[n][p] = matrix_value[n][p - 1] + n*(n+1)*(p)//2
    
    near = limit
    result = 0
    for n in range(2, max_row + 1):
        for p in range(2, n + 1):
            if abs(matrix_value[n][p] - limit) < near:
                near = abs(matrix_value[n][p] - limit)
                result = n*p
    return result
    

#Test & Result


begin_problem = time.time()
problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""
string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
