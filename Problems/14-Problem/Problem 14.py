import time 


problem_number = 14
test_input = 14
test_solution = 9
problem_input = 1000000


#Solution


def solution(limit):
    max_time = 0
    max_starting_integer = 0
    
    for index in range(1, limit+1):
        time = 0
        integer = index
        while integer != 1:
            time += 1
            if integer%2 == 0:
                integer = integer//2
            else:
                integer = 3*integer+1
        
        if max_time < time:
            max_time = time
            max_starting_integer = index
        
    return max_starting_integer


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