import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import gcd


problem_number = 33


#Solution


def solution():
    product_a = 1
    product_b = 1
    for a in range(10, 100):
        for b in range(a + 1, 100):
            a_1 = int(str(a)[0])
            a_2 = int(str(a)[1])
            b_1 = int(str(b)[0])
            b_2 = int(str(b)[1])
            if a_1 == b_1 and a_2 * b == a * b_2:
                product_a *= a
                product_b *= b
            if a_2 == b_2 and a_1 * b == a * b_1 and a_2 != 0:
                product_a *= a
                product_b *= b
            if a_1 == b_2 and a_2 * b == a * b_1:
                product_a *= a
                product_b *= b
            if a_2 == b_1 and a_1 * b == a * b_2:
                product_a *= a
                product_b *= b
    
    return product_b//gcd(product_b, product_a)

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
