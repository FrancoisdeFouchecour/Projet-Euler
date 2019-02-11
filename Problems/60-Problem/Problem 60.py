import time 
import numpy as np 
from collections import defaultdict

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import sieve_for_primes_to
from algorithm import quick_search
from Born_Kerbosch import find_cliques


problem_number = 60


def sub_prime(n, sub_primes):
    string = str(n)
    if len(string) == 1:
        return []
    result = []
    for i in range(len(string) - 1):
        left_num = int(string[:i + 1])
        right_num = int(string[i + 1:])
        if quick_search(sub_primes, left_num) and quick_search(sub_primes, right_num) and quick_search(sub_primes, int(str(right_num)+str(left_num))):
            if len(string) == len(str(left_num)) + len(str(right_num)):
                result.append((left_num, right_num))
    return result


#Solution


def solution(): 
    LIMIT = 8
    prime = sieve_for_primes_to(10**LIMIT)
    
    couple = set()
    
    for p in prime:
        add_list = sub_prime(p, prime)
        for left, right in add_list:
            couple.add((left,right))
    
    graph_dict = defaultdict(list)
    for left, right in couple:
        graph_dict[left].append(right)
        graph_dict[right].append(left)
    
    max_clique = -1
    result = np.infty
    for clique in find_cliques(graph_dict):
        if max_clique <= len(clique):
            if max_clique == len(clique):
                if sum(clique) < result:
                    result = sum(clique)
            else:
                max_clique = len(clique)
                result = sum(clique)
                    
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
