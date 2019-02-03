import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from algorithm import quick_search, quick_add


problem_number = 92
problem_input = 10000000


#Solution


def solution(limit):
    one_list = [1]
    eighty_nine_list = [89]
    for num in range(1, limit):
        new_list = []
        begin = num
        while not(quick_search(one_list, begin)) and not(quick_search(eighty_nine_list, begin)):
            new_list.append(begin)
            after = 0
            for char in str(begin):
                after += int(char)**2
            begin = after
        
        if quick_search(one_list, begin):
            for new in new_list:
                index = quick_add(one_list, new)
                one_list.insert(index, new)
    
        if quick_search(eighty_nine_list, begin):
            for new in new_list:
                index = quick_add(eighty_nine_list, new)
                eighty_nine_list.insert(index, new)

    return len(eighty_nine_list)


def solution2(limit):
    save_list = []
    result = 0
    
    for num in range(1, 7*9*9 + 1):
        begin = num
        while begin != 1 and begin != 89:
            save = 0 
            for char in str(begin):
                save += int(char)**2
            begin = save
        if begin == 89:
            save_list.append(num)
    
    for i in range(1, limit):
        save = 0 
        for char in str(i):
            save += int(char)**2
        if save in save_list:
            result += 1
        
    return result


#Test & Result


begin_problem = time.time()
problem_value = solution2(problem_input)
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
