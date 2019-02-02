import time 


problem_number = 52


def is_permutation(a, b):
    if len(a) == 0 and len(b) == 0:
        return(True)
    elif len(a) != len(b):
        return(False)
    if a[0] in b:
        return(is_permutation(a[1:], b[:b.index(a[0])]+b[b.index(a[0])+1:]))
    else:
        return(False)

#Solution


def solution():
    result = []
    for i in range(10**5, 2*(10**5)):
        if is_permutation(str(i), str(2 * i)) and is_permutation(str(i), str(3 * i)) and is_permutation(str(i), str(4 * i)) and is_permutation(str(i), str(5 * i)) and is_permutation(str(i), str(6 * i)):
            result.append(i)
    return result[0]
    

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
