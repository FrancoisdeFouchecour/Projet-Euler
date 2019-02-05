import time 


problem_number = 493
    

#Solution


def solution():
    binomial_matrix = [[0 for j in range(21)] for i in range(71)]
    
    for i in range(71):
        binomial_matrix[i][0] = 1
    
    for n in range(1, 71):
        for k in range(1, 21):
            binomial_matrix[n][k] = binomial_matrix[n - 1][k - 1] + binomial_matrix[n - 1][k]
    
    N_2 = 0
    for i in range(1, 11):
        N_2 += binomial_matrix[10][i]*binomial_matrix[10][20 - i]
    N_2 *= binomial_matrix[7][2]

    N_3 = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if 20 - i -j > 0:
                N_3 += binomial_matrix[10][i]*binomial_matrix[10][j]*binomial_matrix[10][20 - i - j]
    N_3 *= binomial_matrix[7][3]  
    
    N_4 = 0
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                if 20 - i - j - k > 0: 
                    N_4 += binomial_matrix[10][i]*binomial_matrix[10][j]*binomial_matrix[10][k]*binomial_matrix[10][20 - i - j - k]
    N_4 *= binomial_matrix[7][4]    
    
    N_5 = 0
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                for l in range(1, 11):
                    if 20 - i - j - k - l > 0: 
                        N_5 += binomial_matrix[10][i]*binomial_matrix[10][j]*binomial_matrix[10][k]*binomial_matrix[10][l]*binomial_matrix[10][20 - i - j - k - l]
    N_5 *= binomial_matrix[7][5]   
    
    N_6 = 0
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                for l in range(1, 11):
                    for m in range(1, 11):
                        if 20 - i - j - k - l - m > 0:
                            N_6 += binomial_matrix[10][i]*binomial_matrix[10][j]*binomial_matrix[10][k]*binomial_matrix[10][l]*binomial_matrix[10][m]*binomial_matrix[10][20 - i - j - k - l - m]
    N_6 *= binomial_matrix[7][6]   
    
    N_7 = 0
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                for l in range(1, 11):
                    for m in range(1, 11):
                        for n in range(1, 11):
                            if 20 - i - j - k - l - m - n > 0:
                                N_7 += binomial_matrix[10][i]*binomial_matrix[10][j]*binomial_matrix[10][k]*binomial_matrix[10][l]*binomial_matrix[10][m]*binomial_matrix[10][n]*binomial_matrix[10][20 - i - j - k - l - m - n]
    N_7 *= binomial_matrix[7][7]   
    
    result = sum([N_2*2, N_3*3, N_4*4, N_5*5, N_6*6, N_7*7])/binomial_matrix[70][20]
    result = int(result*(10**9))/10**9
            
    return result


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""


begin_problem = time.time()
problem_value = solution()
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
 