import time 


problem_number = 89
test_solution = 1


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()

test = raw_data.split('\n')


#Solution


def solution(list_input):
    result = 0    
    for num in list_input:
        if num.count('I') == 4:
            if num.count('V') == 0:
                result += 2                
            else:
                result += 3
            
        if num.count('X') == 4:
            if num.count('L') == 0:
                result += 2                
            else:
                result += 3
                            
    return result


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_test = time.time()
test_value = solution(['XIIII', 'XVI'])
end_test = time.time()
test_time = end_test - begin_test

string += "TEST #1\n\n"
string += "Output: "+str(test_value)+"\n"
string += "Answer: "+str(test_solution)+"\n"
string += "Computation time: "+str(test_time)+" sec\n"
string += "Verification: "

if(test_value == test_solution):
    string += "TRUE"
else:
    string += "FALSE"
    

begin_problem = time.time()
problem_value = solution(test)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "\n\n\nRESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
