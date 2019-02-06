import time 


problem_number = 62
test_input = 3
test_solution = 41063625 
problem_input = 5


def is_permutation(a, b):
    if len(a) == 0 and len(b) == 0:
        return(True)
    elif len(a) != len(b):
        return(False)
    if a[0] in b:
        return(is_permutation(a[1:], b[:b.index(a[0])]+b[b.index(a[0])+1:]))
    else:
        return(False)


#Solution


def solution(limit):
    max_permutation = 1
    max_number = 0
    cubic_index = 3
    cubic_exp = 1
    
    while max_permutation < limit and cubic_exp <= 11:
        cubic_exp += 1
        cube = []
        while cubic_index ** 3 < 10**cubic_exp:
            cube.append(cubic_index **3)
            cubic_index += 1
        
        for num in cube:
            number = 0
            for comp in cube:
                if is_permutation(str(num), str(comp)):
                    number += 1
            if number > max_permutation:
                max_number = num
                max_permutation = number
                
    return max_number
    

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
