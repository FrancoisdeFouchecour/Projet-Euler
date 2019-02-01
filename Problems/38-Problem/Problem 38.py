import time 


problem_number = 38


def is_pandigital(string):
    digits = [i for i in range(1, 10)]
    b = True
    for dig in digits:
        b = b and (string.count(str(dig)) == 1)         
    return b


#Solution


def solution():
    result = []
    for n in range(2, 10):
        for i in range(10**(9//n - 1), 10**(9//n)):
            string = ""
            for j in range(1, n + 1):
                string += str(j * i)
            if is_pandigital(string):
                result.append(int(string))
        
    return max(result)

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
