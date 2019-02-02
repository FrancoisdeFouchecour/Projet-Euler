import time 


problem_number = 57
problem_input = 1000


#Solution


def solution(limit):
    result = 0
    N = 1
    D = 1
    
    for n in range(limit):
        N, D= 2*D + N, N + D
        if len(str(N)) == len(str(D)) + 1:
            result += 1
    return result
    

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
