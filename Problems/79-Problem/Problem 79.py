import time 
import numpy as np


problem_number = 79


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()

index = 2
number = 0
number_list = []
for char in raw_data:
    if char == '\n':
        if not(number in number_list):
            number_list.append(number)
        number = 0
        index = 2
    else:
        number += int(char)*10**index
        index -= 1


#Solution


def solution(input_list):
    digits = [[[],[]] for i in range(10)]
    
    for num in input_list:
        first = int(str(num)[0])
        second = int(str(num)[1])
        third = int(str(num)[2])
        
        if not(second in digits[first][1]):
            digits[first][1].append(second)
        if not(third in digits[second][1]):
            digits[second][1].append(third)
        if not(first in digits[second][0]):
            digits[second][0].append(first)
        if not(second in digits[third][0]):
            digits[third][0].append(second)
    
    number_of_digits = 0
    
    for tab in digits:
        if len(tab[0]) + len(tab[1]) > 0:
            number_of_digits += 1
    
    password = []
    
    for i in range(number_of_digits - 2):
        new_digit = -1
        for tab_index in range(len(digits)):
            if len(digits[tab_index][0]) == 0 and len(digits[tab_index][1]) > 0:
                password.append(tab_index)
                new_digit = tab_index
                
        for tab in digits:
            if new_digit in tab[0]:
                tab[0].remove(new_digit)
            if new_digit in tab[1]:
                tab[1].remove(new_digit)
        digits[new_digit] = [[], []]
        
    up = -1
    down = -1
    for tab_index in range(len(digits)):
        if len(digits[tab_index][0]) > 0:
            down = tab_index
    for tab_index in range(len(digits)):
        if len(digits[tab_index][1]) > 0:
            up = tab_index
    
    password += [up, down]
    
    result = ""
    for i in range(len(password)):
        result += str(password[i])
    
    return int(result)


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(number_list)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
