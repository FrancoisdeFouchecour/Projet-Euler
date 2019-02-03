import time 
import numpy as np


problem_number = 59


def decimal_to_binar(n):
    if n == 0:
        return 0
    return n%2 + 10*decimal_to_binar(n//2)


def binar_to_decimal(n):
    if n == 1 or n == 0:
        return n
    else:
        return int(str(n)[-1]) + 2* binar_to_decimal(int(str(n)[:-1]))


def XOR(A, B):
    a = str(decimal_to_binar(A))
    b = str(decimal_to_binar(B))
    while len(a) < len(b):
        a = '0'+a
    while len(a) > len(b):
        b = '0'+b
    
    c = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            c += '0'
        else:
            c += '1'
    return binar_to_decimal(c)


def decipher(text, key):
    plain_text = ""
    for i in range(len(text)):
        plain_text += chr(XOR(text[i], key[i%3]))
    return plain_text


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()

list_name = []
word = ""

for char in raw_data:
    if char == ',':
        list_name.append(int(word))
        word = ""
    elif char == '\n':
        list_name.append(int(word))
    elif char != '"':
        word += char


#Solution


def solution(input_list):
    result = 0
    length = len(input_list)
    normal_frequency = [11.682, 4.434, 5.238, 3.174, 2.799, 4.027, 1.642, 4.200, 7.294, 0.511, 0.456, 2.415, 3.826, 2.284, 7.631, 4.319, 0.222, 2.826, 6.686, 15.978, 1.183, 0.824, 5.497, 0.045, 0.763, 0.045]
    score = np.infty
    
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                key = [a, b, c]
                new_text = [0 for i in range(length)]
                for i in range(len(new_text)):
                    new_text[i] = XOR(input_list[i], key[i%3])
                
                letter_frequency = [[0 for j in range(26)] for i in range(3)]
                
                for i in range(len(new_text)):
                    if 65 <= new_text[i] and new_text[i] <= 90:
                        letter_frequency[i%3][new_text[i] - 65] += 1
                    elif 97 <= new_text[i] and new_text[i] <= 122:
                        letter_frequency[i%3][new_text[i] - 97] += 1

                new_score = 0
                for i in range(3):
                    for j in range(26):
                        letter_frequency[i][j] = letter_frequency[i][j]/(length//3)
                        new_score += abs(letter_frequency[i][j] - normal_frequency[j])
                
                if new_score < score:
                    score = new_score
                    result = sum(new_text)
                
    return result


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
