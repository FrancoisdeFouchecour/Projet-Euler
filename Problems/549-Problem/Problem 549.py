import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import min_factor


problem_number = 549
test_input = 100
test_solution = 2012
problem_input = 100000000


def expo(num, div):
    if num%(div**2) == 0:
        return 1 + expo(num//div, div)
    else:
        return 1


#Solution


def solution(limit):
    factors = min_factor(limit)
    tab_s = [0 for _ in range(limit + 1)]
    
    for n in range(2, limit + 1):
        if factors[n] == n:
            tab_s[n] = n
        else:
            k = expo(n, factors[n])
            if factors[n]**k == n:
                nb_p = 1
                mult = 1
                while nb_p < k:
                    mult += 1
                    nb_p += 1
                    if mult%factors[n] == 0:
                        nb_p += expo(mult, factors[n])
                tab_s[n] = mult * factors[n]
                #print(n, tab_s[n], mult, nb_p)
            else:
                div = factors[n]**k
                tab_s[n] = max(tab_s[div], tab_s[n//div])
    
    return sum(tab_s)


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value = solution(test_input)
end_test = time.time()
test_time = end_test - begin_test

string += "TEST #1\n\n"
string += "Input: "+str(test_input)+"\n"
string += "Output: "+str(test_value)+"\n"
string += "Answer: "+str(test_solution)+"\n"
string += "Computation time: "+str(test_time)+" sec\n"
string += "Verification: "

if(test_value == test_solution):
    string += "TRUE"
else:
    string += "FALSE"
    

begin_problem = time.time()
problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "\n\n\nRESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
