import time 
import numpy as np


problem_number = 686
problem_input_str = 123
problem_input_value = 678910

#Solution


def solution(L, n):
    log2 = np.log(2)/np.log(10)
    logDown = np.log(L/(10**(len(str(L))-1)))/np.log(10)
    logUp = np.log((L+1)/(10**(len(str(L))-1)))/np.log(10)
    count = 0 
    st = 0
    iter = 0
    while count < n:
        st += log2
        if st >= 1:
            st -=1
        if (st > logDown) and (st < logUp):
            count +=1
        iter += 1
    return (iter)
    

#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(problem_input_str, problem_input_value)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input_str)+" ; "+str(problem_input_value)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"
string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
