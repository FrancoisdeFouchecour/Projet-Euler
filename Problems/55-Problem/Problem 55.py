import time 


problem_number = 55
problem_input = 10000


#Solution


def solution(limit):
    result = 0
    for i in range(1, limit):
        b = False
        num = i
        j = 0 
        while j < 50 and not(b):
            j += 1
            num = num + int(str(num)[::-1])
            if num == int(str(num)[::-1]):
                b = True
        
        if not(b):
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
