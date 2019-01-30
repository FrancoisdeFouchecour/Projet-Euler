import time 

problem_number = 8
test_input = 4
test_solution = 5832 
problem_input = 13


#Solution


number_file = open("data.txt", "r")
raw_number = number_file.read()
number_file.close()

def solution(string_number, limit):
    length = len(string_number)
    highest_count = 0
    
    for begin_index in range(length-limit):
        count = 1
        for sub_index in range(limit):
            count *= int(string_number[begin_index+sub_index])
        if count > highest_count:
            highest_count = count
        
    return highest_count


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value = solution(raw_number, test_input)
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
problem_value = solution(raw_number, problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "\n\n\nRESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()