import time 
import numpy as np


problem_number = 102


#read data


number_file = open("data.txt", "r")
raw_data = number_file.read()
number_file.close()

raw_data = raw_data.split('\n')
triangle_list = []
for tri in raw_data:
    triangle_list.append(tri.split(','))

for i in range(len(triangle_list)):
    for j in range(len(triangle_list[i])):
        triangle_list[i][j] = int(triangle_list[i][j])


#Solution


def solution(input_list):
    result = 0
    for triangle in input_list:
        theta_a, theta_b, theta_c= 0 , 0, 0
        
        if triangle[0] >= 0 and triangle[1] >= 0:
            theta_a = np.arctan(triangle[1]/triangle[0])
        if triangle[0] >= 0 and triangle[1] < 0:
            theta_a = 2*np.pi + np.arctan(triangle[1]/triangle[0])
        if triangle[0] < 0 and triangle[1] >= 0:
            theta_a = np.pi + np.arctan(triangle[1]/triangle[0])
        if triangle[0] < 0 and triangle[1] < 0:
            theta_a = np.pi + np.arctan(triangle[1]/triangle[0])

        if triangle[2] >= 0 and triangle[3] >= 0:
            theta_b = np.arctan(triangle[3]/triangle[2])
        if triangle[2] >= 0 and triangle[3] < 0:
            theta_b = 2*np.pi + np.arctan(triangle[3]/triangle[2])
        if triangle[2] < 0 and triangle[3] >= 0:
            theta_b = np.pi + np.arctan(triangle[3]/triangle[2])
        if triangle[2] < 0 and triangle[3] < 0:
            theta_b = np.pi + np.arctan(triangle[3]/triangle[2])

        if triangle[4] >= 0 and triangle[5] >= 0:
            theta_c = np.arctan(triangle[5]/triangle[4])
        if triangle[4] >= 0 and triangle[5] < 0:
            theta_c = 2*np.pi + np.arctan(triangle[5]/triangle[4])
        if triangle[4] < 0 and triangle[5] >= 0:
            theta_c = np.pi + np.arctan(triangle[5]/triangle[4])
        if triangle[4] < 0 and triangle[5] < 0:
            theta_c = np.pi + np.arctan(triangle[5]/triangle[4])

        sup = max(theta_a, theta_b)
        inf = min(theta_a, theta_b)
        
        theta_c_test = theta_c + np.pi
        if theta_c_test > 2*np.pi:
            theta_c_test -= 2*np.pi
            
        if sup - inf < np.pi:
            if inf <= theta_c_test and theta_c_test <= sup:
                result +=1
        
        if sup - inf >= np.pi:
            if sup <= theta_c_test or inf >= theta_c_test:
                result += 1
                
    return result


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(triangle_list)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
