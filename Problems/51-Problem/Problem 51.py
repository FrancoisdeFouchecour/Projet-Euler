import time 
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),'Utils'))
from arithm import is_prime


problem_number = 51

        
def family(stars, num):
    number = 0
    if stars[0] == 0:
        for digits in range(10):
            test = ''
            index = 0
            for bo in stars:
                if bo == 0:
                    test += str(num)[index]
                    index += 1
                else:
                    test += str(digits)
            if is_prime(int(test)) == int(test):
                number += 1
    else:
        for digits in range(1, 10):
            test = ''
            index = 0
            for bo in stars:
                if bo == 0:
                    test += str(num)[index]
                    index += 1
                else:
                    test += str(digits)
            if is_prime(int(test)) == int(test):
                number += 1
    return number


#Solution


def solution():    
    #for a 8-familiy, there is 3, 6, 9, 12, ... repating digits, lets see first for 3 first
    #if the candidate has 4 digits
    max_prime = 0
    prime_star = 0
    num = 0
    
    four_digits_star = [1, 1, 1, 0]
    for first_digits in [1, 3, 5, 7, 9]:
        if family(four_digits_star, first_digits) > max_prime:
            max_prime = family(four_digits_star, first_digits)
    
    #lets do it for 5 digits
    five_digits_star = [[1, 1, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 1, 0], [0, 1, 1, 1, 0]]
    for stars in five_digits_star:
        for first_digits in [1, 3, 5, 7, 9]:
            for second_digits in range(1, 10):
                if family(stars, first_digits + second_digits*10) > max_prime:
                    max_prime = family(stars, first_digits + second_digits*10)
                    prime_star = stars
                    num = first_digits + second_digits*10
                        
    #lets do it for 6 digits
    six_digits_star = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 1, 1, 0, 1, 0], [0, 1, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0]]
    for stars in six_digits_star:
        for first_digits in [1, 3, 5, 7, 9]:
            for second_digits in range(11, 100):
                if family(stars, first_digits + second_digits*10) > max_prime:
                    max_prime = family(stars, first_digits + second_digits*10)
                    prime_star = stars
                    num = first_digits + second_digits*10
                    
    test = ''
    index = 0
    for bo in prime_star:
        if bo == 0:
            test += str(num)[index]
            index += 1
        else:
            test += str(1)
            
    return int(test)


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
