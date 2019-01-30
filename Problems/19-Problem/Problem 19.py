import time 


problem_number = 19


def is_leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False
    

def is_end_of_month(date):
    if date[1] in [8, 3, 5, 10]:
        return (date[0] == 29)
    elif date[1] in [0, 2, 4, 6, 7, 9, 11]:
        return (date[0] == 30)
    elif date[1] == 1:
        if is_leap_year(date[2]):
            return (date[0] == 28)
        else:
            return (date[0] == 27)
    return True

#Solution


def solution(start_day, start_month, start_year, start_day_of_week):
    current_date = [start_day, start_month, start_year, start_day_of_week]
    result = 0
    
    while current_date[2] < 2001:
        if is_end_of_month(current_date):
            if current_date[1] == 11:
                current_date[0] = 0
                current_date[1] = 0
                current_date[2] += 1
            else:
                current_date[0] = 0
                current_date[1] += 1
        else:
            current_date[0] += 1
        current_date[3] = (current_date[3] + 1)%7
        
        if current_date[3] == 6 and current_date[2] > 1900 and current_date[2] < 2001 and current_date[0] == 0:
            result += 1

    return result


#Test & Result


fichier = open("Solution "+str(problem_number)+".txt", "w")
string = ""

begin_problem = time.time()
problem_value = solution(0, 0, 1900, 0)
end_problem = time.time()
problem_time = end_problem - begin_problem

string += "RESULT PROBLEM #"+str(problem_number)+"\n\n"
string += "Input: 1 Jan 1900 was a Monday\n"
string += "Output: "+str(problem_value)+"\n"
string += "Computation time: "+str(problem_time)+" sec\n"

string += "\n\n\nCurrent date & time: " + time.strftime("%c")

fichier.write(string)
fichier.close()
