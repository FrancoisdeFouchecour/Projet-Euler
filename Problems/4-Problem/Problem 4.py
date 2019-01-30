import time 


problem_number = 4
test_input = 2
test_solution = 9009
problem_input = 3


#Solution


def is_palindrome(number):
    string_num = str(number)
    length = len(string_num)
    for i in range(length//2):
        if string_num[i] != string_num[length-1-i]:
            return(False)
    return(True)
    

def solution(limit):
    highest_palindrome = 0
    for i in reversed(range(1,10**limit)):
        for j in reversed(range(1, 10**limit)):
            current = i*j
            if current > highest_palindrome and is_palindrome(current):
                highest_palindrome = current
    return highest_palindrome


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