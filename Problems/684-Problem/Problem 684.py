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
    
def s(n, modulo):
    quotien = n//9
    rest = n%9
    nombre = expo_rapide(10, quotien, modulo)
    return (nombre - 1 + rest*nombre)%modulo


def S(k, modulo):
    if k <= 9:
        return ((k*(k+1))//2)%modulo
    else:
        q, r = k//9, k%9
        mult = (6*expo_rapide(10, q, modulo) - 9*(q-1) - 15)%modulo 
        mult += (r*(r+1))//2*expo_rapide(10, q, modulo)
        mult = mult%modulo
        mult += r*(expo_rapide(10, q, modulo)-1)
        mult = mult%modulo
        return mult


#Solution


def solution(limit, modulo):
    fib = 1
    fib_prec = 1
    sumation = 0

    for i in range (2, limit+1):
        sumation += S(fib, modulo)
        print(i, fib, sumation)
        fib , fib_prec = fib + fib_prec , fib 
    return sumation
    

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
