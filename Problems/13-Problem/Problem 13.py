import time 

problem_number = 13
problem_input = 10


#Solution


number_file = open("data.txt", "r")
raw_text = number_file.read()
number_list = [int(raw_text[i*51:i*51+50]) for i in range(100)]
        

def solution(data_list, limit):
    result = 0
    for num in data_list:
        result += num

    return str(result)[0:10]


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""
    

begin_problem = time.time()
problem_value = solution(number_list, problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()