import time 

problem_number = 11
problem_input = 4


#Solution


number_file = open("data.txt", "r")
raw_grid = number_file.read()
number_file.close()

grid = [[0 for j in range(20)] for i in range(20)]
for i in range(20*20*3):
    if i%3 == 0:
        grid[i//60][i%60//3] += int(raw_grid[i])*10
    if i%3 == 1:
        grid[i//60][i%60//3] += int(raw_grid[i])
        

def solution(grid_number, limit):
    highest_mult = 0
    #horizontal
    for i in range(20):
        for j in range(20-limit+1):
            mult = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            if mult > highest_mult:
                highest_mult = mult


    #vertical
    for i in range(20-limit+1):
        for j in range(20):
            mult = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
            if mult > highest_mult:
                highest_mult = mult
    
    #diagonal (left-right)
    for i in range(20-limit+1):
        for j in range(20-limit+1):
            mult = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if mult > highest_mult:
                highest_mult = mult

    #diagonal (right-left)
    for i in range(20-limit+1):
        for j in range(limit-1,20):
            mult = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
            if mult > highest_mult:
                highest_mult = mult

    return highest_mult


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""
    

begin_problem = time.time()
problem_value = solution(grid, problem_input)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: "+str(problem_input)+"\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()