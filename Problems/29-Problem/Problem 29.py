import time 


problem_number = 29
test_input = 5
test_solution = 15
problem_input = 100


def south_east(n):
    return(4*n**2 - 2*n +1)

def south_west(n):
    return(4*n**2 + 1)

def north_west(n):
    return(4*n**2 + 2 * n + 1)

def north_east(n):
    return(4*n**2 + 4 * n + 1)

    
#Solution


def solution(limit):
    result = []
    for a in range(2, limit + 1):
        for b in range(2, limit + 1):
            if result.count(a**b) == 0:
                result.append(a**b)
            
    return len(result)

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
