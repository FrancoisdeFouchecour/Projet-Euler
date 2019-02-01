import time 


problem_number = 40


def d(n):
    dec_index = 1
    before = 0
    after = 9    
    while n > after:
        dec_index += 1
        after, before = after + dec_index*(10**dec_index - 10**(dec_index - 1)), after
    return int(str(10**(dec_index - 1) + ((n - before - 1)//dec_index))[(n - before - 1)%dec_index])


#Solution


def solution():
    return d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000)

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
