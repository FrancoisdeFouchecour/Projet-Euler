def two_sum(Set, target):
    #Return True if two value of Set sum to value (Set is ordered)
    size = len(Set)
    i = 0
    j = size - 1
    x = Set[i] + Set[j]
    
    while i != j:
        if x < target:
            i += 1
            x = Set[i] + Set[j]
        elif x > target:
            j -= 1
            x = Set[i] + Set[j]
        elif x == target:
            return(True)
    return(False)
    