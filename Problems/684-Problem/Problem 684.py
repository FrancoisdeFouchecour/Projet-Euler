import time 


problem_number = 684
problem_input = 90
problem_modulo = 1000000007


def expo_rapide(n, exp, modulo):
    if exp == 0:
        return 1
    elif exp == 1:
        return n%modulo
    elif exp%2 == 0:
        sqrt = expo_rapide(n, exp//2, modulo)
        return((sqrt*sqrt)%modulo)
    else:
        sqrt = expo_rapide(n, exp//2, modulo)
        return((n*sqrt*sqrt)%modulo)


#Solution


def solution(limit, modulo):
    fib = 1
    fib_prec = 1
    sumation = 0
    for i in range (2, limit+1):
        q, r = fib//9, fib%9
        sumation += (expo_rapide(10, q, modulo)*(6 + (r*(r+3))//2) - 9*(q-1) - 15 - r)%modulo
        fib , fib_prec = fib + fib_prec , fib 
    return sumation%modulo
    

#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(problem_input, problem_modulo)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
