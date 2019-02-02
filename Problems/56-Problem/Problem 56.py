import time 


problem_number = 56
problem_input = 100


#Solution


def solution(limit):
    result = 0
    for a in range(1, limit):
        for b in range(1, limit):
            digital_count = 0
            for char in str(a**b):
                digital_count += int(char)
            
            if digital_count > result:
                result = digital_count
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
