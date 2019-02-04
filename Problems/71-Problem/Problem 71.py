import time 


problem_number = 71
test_input = 8
test_solution = 2
problem_input = 1000000


#Solution


def solution(limit):
    min_limit = 3/7
    min_n = 0
    target = 3/7
    for d in range(2, limit + 1):
        n = 0 
        if not(d%7 == 0):
            n = int(3*d/7)
        if target - n/d < min_limit:
            min_limit = target - n/d
            min_n = n
    return min_n


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
