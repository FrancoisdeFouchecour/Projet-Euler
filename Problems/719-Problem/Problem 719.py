import time 


problem_number = 719
test_input = 10**4
test_solution = 41333
problem_input = 10**12


def is_S(n):
    return True


def sub_sum(number):
    n = 1
    while 10**n <= number:
        n+= 1
    
    if n==1:
        return {number}
    else:
        set_conso = {number}
        for i in range(1,n):
            left_set, right_set = sub_sum(number//(10**i)), sub_sum(number%(10**i))
            #print(left_set, right_set)
            for left in left_set:
                for right in right_set:
                    set_conso.add(left + right)
        return set_conso
    

#Solution


def solution(N):
    sumation = 0
    
    index = 4
    square = 16

    while square <= N:
        if index in sub_sum(square):
            sumation += square
            print(index, square)
        
        index +=1
        square = index*index
        
    return sumation
    

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