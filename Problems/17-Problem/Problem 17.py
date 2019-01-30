import time 


problem_number = 17
test_input = 5
test_solution = 19
problem_input = 1000


#Solution
STRING_UNIT = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
STRING_DEC = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

def number_to_letter(number):
    number_letter = 0
    num_length = len(str(number))
    
    if num_length == 1:
        number_letter = STRING_UNIT[number]
    elif num_length == 2:
        if number < 20:
            number_letter += STRING_UNIT[number]
        else:
            number_letter += STRING_DEC[number//10] + STRING_UNIT[number%10]
    elif num_length == 3:
        number_letter += STRING_UNIT[number//100] + len("hundred")
        if number%100 != 0:
             number_letter += len("and") + number_to_letter(number%100)
    elif num_length == 4:
        number_letter += STRING_UNIT[number//1000] + len("thousand") + number_to_letter(number%1000)
        
    return number_letter

def solution(limit):
    result = 0
    for i in range(1, limit + 1):
        result += number_to_letter(i)

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