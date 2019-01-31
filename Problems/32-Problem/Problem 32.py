import time 


problem_number = 32


def is_pandigital(a, b, c):
    string = str(a) + str(b) + str(c)
    digits = [i for i in range(1, 10)]
    b = True
    
    for dig in digits:
        b = b and (string.count(str(dig)) == 1)
            
    return b


#Solution


def solution():
    product_memory = []
    #si a*b=c et a<b, a est compris entre 1 et 99
    for a in range(1, 10):
        for b in range(1000, 10000):
            c = a * b
            if len(str(c)) == 4:
                if is_pandigital(a, b, c) and product_memory.count(c) == 0:
                    product_memory.append(c)
                    
    
    for a in range(10, 100):
        for b in range(100, 1000):
            c = a * b
            if len(str(c)) == 4:
                if is_pandigital(a, b, c) and product_memory.count(c) == 0:
                    product_memory.append(c)
                    
    return sum(product_memory)

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
