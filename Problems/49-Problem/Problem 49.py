import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime


problem_number = 49


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
    prime_possible = [i for i in range(1000, 10000) if is_prime(i) == i]
    count = 0
    result = 0
    for prime_1 in prime_possible:
        for prime_2 in prime_possible:
            prime_3 = 2 * prime_2 - prime_1
            if prime_1 < prime_2 and is_permutation(str(prime_1), str(prime_2)) and is_permutation(str(prime_1), str(prime_3)) and prime_3 in prime_possible:
                count += 1
                if count == 2:
                    result = int(str(prime_1)+str(prime_2)+str(prime_3))
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
