import time 


problem_number = 30
test_input = 4
test_solution = 19316
problem_input = 5

    
def is_sum(power, number):
    result = 0
    for char in str(number):
        result += power[int(char)]
    
    return result == number


#Solution


def solution(limit):
    result = 0
    power = [i**limit for i in range(10)]
    exp_limit = 2
    while exp_limit*power[9] - 10**exp_limit > 0:
        exp_limit += 1
    
    for i in range(2, 10**exp_limit):
        if is_sum(power, i):
            result += i
    
    return result

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
