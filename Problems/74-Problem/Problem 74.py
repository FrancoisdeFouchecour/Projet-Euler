import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import factorial


problem_number = 74
problem_input = 1000000


def solution_problem_34():
    result = []
    fact_tab = [factorial(i) for i in range(10)]
    for num in range(3, 1000000):
        digit_sum = 0
        for char in str(num):
            digit_sum += fact_tab[int(char)]
        if digit_sum == num:
            result.append(num)        
    return result
    
    
#Solution


def solution(limit):
    fact_tab = [factorial(i) for i in range(10)]
    tab_result = [0 for i in range(10*limit + 1)]
    
    tab_result[1] = 1
    tab_result[2] = 2
    tab_result[145] = 1
    tab_result[40585] = 1
    
    tab_result[871] = 2
    tab_result[45361] = 2
    tab_result[872] = 2
    tab_result[45362] = 2
    
    tab_result[169] = 3
    tab_result[363601] = 3
    tab_result[1454] = 3
    
    for i in range(limit + 1):
        if tab_result[i] == 0:
            new_tab = []
            
            current = i
            next_num = i
            
            while next_num < limit and tab_result[next_num] == 0:
                current = next_num
                next_num = 0
                for char in str(current):
                    next_num += fact_tab[int(char)]
                new_tab.append(current)
            
            nb_add = len(new_tab)
            for j in range(nb_add):
                if new_tab[j] <= limit:
                    tab_result[new_tab[j]] = tab_result[next_num] + nb_add - j
    
    result = 0
    for i in range(limit + 1):
        if tab_result[i] == 60:
            print(i) 
            result += 1               
    return result
    

#Test & Result


begin_problem = time.time()
problem_value = solution(problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""
string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
