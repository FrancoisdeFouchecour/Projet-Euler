import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import gcd


problem_number = 64
test_input = 13
test_solution = 4
problem_input = 10000


def next_state(state):
    b = state[1]
    c = state[2]
    N = state[3]
    num = c
    dem = N - b*b
    
    num, dem = num//gcd(num, dem), dem//gcd(num, dem)
    
    assert num == 1
    
    target = int(N**0.5)
    k = 0
    
    while b - (k + 1)*dem >= - target:
        k += 1
    
    return [k, k*dem - b,dem , N]


def len_cycle(N):
    save = []
    target = int(N**0.5)
    if target**2 == N:
        return 0
        
    state = next_state([target, target, 1, N])
    save.append(state)
    k = 1
    next_s = next_state(state)
    
    while not(next_s in save):
        save.append(next_s)
        next_s = next_state(next_s)
        k += 1
    
    return k


#Solution


def solution(limit):
    result = 0
    for N in range(2, limit + 1):
        if len_cycle(N)%2 == 1:
            result += 1
            
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
