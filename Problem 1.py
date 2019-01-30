#Solution

def solution(limit):
    count = 0

    for i in range(1, limit):
        if (i%3 == 0) or (i%5 == 0):
            count += i
            
    return count

#Test

assert solution(10) == 23

#Result

print(solution(1000))
