import time 


problem_number = 43


def is_pandigital(string):
    b = True
    for dig in string:
        b = b and (string.count(str(dig)) == 1)         
    return b


#Solution


def solution():
    possible_number = []
    #3-digits number divisible by 17
    for i in range(100, 1000):
        if i%17 == 0 and is_pandigital(str(i)):
            possible_number.append(i)
        
    new_possible =[]
    #3-digits number divisible by 13
    for num in possible_number:
        for i in range(0, 10):
            if not(str(i) in str(num)) and ((i*10**3 + num)//10)%13 == 0:
                new_possible.append(i*10**3 + num)
    possible_number = new_possible
        
    new_possible =[]
    #3-digits number divisible by 11
    for num in possible_number:
        for i in range(0, 10):
            if not(str(i) in str(num)) and ((i*10**4 + num)//10**2)%11 == 0:
                new_possible.append(i*10**4 + num)
    possible_number = new_possible
    
    new_possible =[]
    #3-digits number divisible by 7
    for num in possible_number:
        for i in range(0, 10):
            if not(str(i) in str(num)) and ((i*10**5 + num)//10**3)%7 == 0:
                new_possible.append(i*10**5 + num)
    possible_number = new_possible
    
    new_possible =[]
    #3-digits number divisible by 5
    for num in possible_number:
        for i in range(0, 10):
            if not(str(i) in str(num)) and ((i*10**6 + num)//10**4)%5 == 0:
                new_possible.append(i*10**6 + num)
    possible_number = new_possible
    
    new_possible =[]
    #3-digits number divisible by 3
    for num in possible_number:
        for i in range(0, 10):
            if not(str(i) in str(num)) and ((i*10**7 + num)//10**5)%3 == 0:
                new_possible.append(i*10**7 + num)
    possible_number = new_possible
    
    new_possible =[]
    #3-digits number divisible by 2
    for num in possible_number:
        for i in range(0, 10):
            if not(str(i) in str(num)) and ((i*10**8 + num)//10**6)%2 == 0 and is_pandigital(str(i*10**8 + num)):
                new_possible.append(i*10**8 + num)
    possible_number = new_possible
    
    result = []
    for num in possible_number:
        if len(str(num)) == 9:
            digits = [i for i in range(10)]
            for dig in str(num):
                digits.remove(int(dig))
            result.append(int(str(digits[0])+str(num)))
    
    return sum(result)

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
