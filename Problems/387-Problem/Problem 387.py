import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime


problem_number = 387
test_input = 4
test_solution = 90619
problem_input = 14


def is_harshad(n):
    return (n%sum([int(char) for char in str(n)]) == 0)


def is_right_truncable_harshad(n):
    if len(str(n)) == 1:
        return False
    if len(str(n)) == 2:
        return is_harshad(n)
    else:
        return is_harshad(n) and is_right_truncable_harshad(int(str(n)[:-1]))


def is_strong_harshad(n):
    if not(is_harshad(n)) or n == 1:
        return False
    else:
        return is_prime(n//sum([int(char) for char in str(n)])) == n//sum([int(char) for char in str(n)])


def is_strong_right_truncable_Harshad(n):
    if not(is_prime(n) == n):
        return False
    else:
        return is_strong_harshad(int(str(n)[:-1])) and is_right_truncable_harshad(int(str(n)[:-1]))

    
#Solution


def solution(limit):
    result = 0
    right_truncable_harshad_tab = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    
    for exp_index in range(limit - 2):    
        new_right_tab = []
        for num in right_truncable_harshad_tab[exp_index]:
            for i in range(10):
                if is_harshad(num*10 + i):
                    new_right_tab.append(num*10 + i)
        right_truncable_harshad_tab.append(new_right_tab)
    
    eligible_number = []
    for i in range(1, limit - 1):
        for num in right_truncable_harshad_tab[i]:
            if is_strong_harshad(num):
                eligible_number.append(num)
    
    for num in eligible_number:
        for digits in range(10):
            test_num = 10*num + digits
            if is_prime(test_num) == test_num:
                result += test_num
                
    return result


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
