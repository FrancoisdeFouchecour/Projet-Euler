import time 


problem_number = 31
test_input = 5
test_solution = 4
problem_input = 200


#Solution


def solution(limit):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    matrix_solution = [[0 for j in range(limit + 1)] for i in range(len(coins))]
    
    for coin_target in range(1, limit + 1):
        for coin_available in range(len(coins)):
            if coin_available == 0:
                matrix_solution[coin_available][coin_target] = 1
            else:
                number_possiblity = 0
                target = coin_target
                for coin_index in range(coin_available + 1):
                    if target - coins[coin_index] > 0:
                        number_possiblity += matrix_solution[coin_index][target - coins[coin_index]]
                    elif target - coins[coin_index] == 0:
                        number_possiblity += 1

                matrix_solution[coin_available][coin_target] = number_possiblity
    
    return matrix_solution[-1][-1]

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
