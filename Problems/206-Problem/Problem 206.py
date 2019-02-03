import time 


problem_number = 206


#Solution


def solution():
    result = 0
    for i in range(10**8, int((2**0.5)*10**8)):
        square = str((10*i)**2)
        if square[2] == '2' and square[4] == '3' and square[6] == '4' and square[8] == '5' and square[10] == '6' and square[12] == '7' and square[14] == '8' and square[16] == '9':
            result = i*10
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
