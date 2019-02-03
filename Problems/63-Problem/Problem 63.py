import time 


problem_number = 63


#Solution


def solution():
    result = 0
    # because 10**(1-1/power) <= x < 10, so if power > 21 there is no solution
    for power in range(1, 22):
        for x in range(1,10):
            if len(str(x**power)) == power:
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
