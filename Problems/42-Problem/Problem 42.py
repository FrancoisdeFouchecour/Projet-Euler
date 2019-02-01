import time 


problem_number = 42


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()

list_name = []
word = ""

for char in raw_data:
    if char == ',':
        list_name.append(word)
        word = ""
    elif char == '\n':
        list_name.append(word)
    elif char != '"':
        word += char


#Solution


def solution(input_list):
    result = []
    triangle = [int(0.5*n*(n+1)) for n in range(1, 30)]
    for w in input_list:
        word_value = 0        
        for letter in w:
            word_value += ord(letter) - ord('A') + 1
        if word_value in triangle:
            result.append(w)
    return len(result)


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(list_name)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
