import time 


problem_number = 301


def X(a, b, c):
    return a^b^c


#Solution


def solution():
    result = 0
    for n in range(1, 2**30 + 1):
        if X(n, 2*n, 3*n) == 0:
            result += 1
    return result


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution()
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
