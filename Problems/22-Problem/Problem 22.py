import time 

problem_number = 22
test_solution = 23


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
    result = 0
    
    for word_index in range(len(input_list)):
        letter_count = 0
        for letter_index in range(len(input_list[word_index])):
            letter_count += ord(input_list[word_index][letter_index]) - ord('A') + 1
        result += letter_count * (1 + word_index)
        
    return result


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(sorted(list_name))
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
