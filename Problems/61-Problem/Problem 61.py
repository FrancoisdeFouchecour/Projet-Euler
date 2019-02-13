import time 


problem_number = 61


def next_possible(current_num, num_list, index_set):
    possible = []
    for i in index_set:
        for num in num_list[i]:
            if current_num%100 == num//100:
                possible.append((i, num))
    return possible


def recur_suite(current_num, num_list, index_set, current_index):
    if len(index_set) == 0:
        return [[(current_num, current_index)]]
    
    possibilities = next_possible(current_num, num_list, index_set)
    if len(possibilities) == 0:
        return [[(current_num, current_index)]]
    result = []
    new_suites = []
    
    for index, num in possibilities:
        new_set = index_set.difference(set([index]))
        new_suites += recur_suite(num, num_list, new_set, index)
    
    for suites in new_suites:
        result.append([(current_num, current_index)]+suites)
    return result

    
#Solution


def solution(): 
    tab_index = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    numb_tab = [[] for i in tab_index]
    
    n = 1
    P = n*(n + 1)//2
    while P < 10000:
        if P >= 1000 and (P%100)//10 != 0:
            numb_tab[3].append(P)
        n += 1
        P = n*(n + 1)//2
    
    n = 1
    P = n*n
    while P < 10000:
        if P >= 1000 and (P%100)//10 != 0:
            numb_tab[4].append(P)
        n += 1
        P = n*n
        
    n = 1
    P = n*(3*n - 1)//2
    while P < 10000:
        if P >= 1000 and (P%100)//10 != 0:
            numb_tab[5].append(P)
        n += 1
        P = n*(3*n - 1)//2
        
    n = 1
    P = n*(2*n - 1)
    while P < 10000:
        if P >= 1000 and (P%100)//10 != 0:
            numb_tab[6].append(P)
        n += 1
        P = n*(2*n - 1)
        
    n = 1
    P = n*(5*n - 3)//2
    while P < 10000:
        if P >= 1000 and (P%100)//10 != 0:
            numb_tab[7].append(P)
        n += 1
        P = n*(5*n - 3)//2
        
    n = 1
    P = n*(3*n - 2)
    while P < 10000:
        if P >= 1000 and (P%100)//10 != 0:
            numb_tab[8].append(P)
        n += 1
        P = n*(3*n - 2)
    
    
    suites_possible = []
    for octo in numb_tab[8]:
        suites_possible += recur_suite(octo, numb_tab, set([3, 4, 5, 6, 7]), 8)
    
    result = 0
    for suites in suites_possible:
        if len(suites) == 6:
            if suites[0][0]//100 == suites[5][0]%100:
                for couple in suites:
                    result += couple[0]
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
