import time 


problem_number = 53


#Solution


def solution():
    result = 0
    Binomial = [[0 for j in range(101)] for i in range(101)]
    for i in range(101):
        Binomial[i][0] = 1
    
    for i in range(1, 101):
        for j in range(1, 101):
            Binomial[i][j] = Binomial[i - 1][j] +Binomial[i - 1][j - 1]
            if Binomial[i][j] > 1000000:
                result +=1
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
