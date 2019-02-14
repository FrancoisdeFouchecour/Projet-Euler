import time 


problem_number = 80
test_input = 2
test_solution = 475
problem_input = 100


def sqrt_devlpt_sum(n):
    d = int(n**0.5)*10**100
    u = (int(n**0.5) + 1)*10**100
    target = n*10**200
    while u - d > 1:        
        if ((u+d)//2)**2 <= target:
            d = (u+d)//2
        else:
            u = (u+d)//2
    
    string = str(d)[:-1]
    result = 0
    for char in string:
        result += int(char)
    return result

#Solution


def solution(limit):
    result = 0
    squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
    for n in range(2, limit + 1):
        if not(n in squares):
            result += sqrt_devlpt_sum(n)
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
