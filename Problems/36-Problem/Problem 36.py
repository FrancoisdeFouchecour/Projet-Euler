import time 

problem_input = 1000000
problem_number = 36


def decimal_to_binar(n):
    if n == 0:
        return 0
    return n%2 + 10*decimal_to_binar(n//2)

#Solution


def solution(limit):
    result = []
    for i in range(limit):
        if str(i) == str(i)[::-1]:
            binar = decimal_to_binar(i)
            if str(binar) == str(binar)[::-1]:
                result.append(i)
    
    return sum(result)

#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
