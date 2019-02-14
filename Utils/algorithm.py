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


def two_sum_index(Set, target):
    #Return index of two value of Set sum to value (Set is ordered)
    size = len(Set)
    if size == 0:
        return []
    i = 0
    j = size - 1
    x = Set[i] + Set[j]
    
    while i < j:
        if x < target:
            i += 1
            x = Set[i] + Set[j]
        elif x > target:
            j -= 1
            x = Set[i] + Set[j]
        elif x == target:
            return([[Set[i], Set[j]]] + two_sum_index(Set[i + 1:j], target))
    return([])

    
def quick_search(Set, x):
    if len(Set) == 0:
        return(False)
    elif len(Set) == 1:
        return(Set[0] == x)
    else:
        min_index = 0
        max_index = len(Set) - 1
        while min_index <= max_index:
            new_index = (max_index + min_index)//2
            if Set[new_index] == x:
                return True
            elif Set[new_index] < x:
                min_index = new_index + 1
            else:
                max_index = new_index - 1
        return(False)


def quick_add(Set, x):
    if len(Set) == 0:
        return(0)
    elif Set[0] > x:
        return(0)
    elif Set[-1] < x:
        return(len(Set))
    else:
        min_index = 0
        max_index = len(Set) - 1
        while min_index <= max_index:
            new_index = (max_index + min_index)//2
            if Set[new_index] == x:
                return new_index
            elif Set[new_index] < x:
                min_index = new_index + 1
            else:
                max_index = new_index - 1
        return(min_index)
    return(0)


def quick_exp_mod(x, n, mod):
    if n == 1:
        return(x%mod)
    elif n == 0:
        return(1)
    elif n%2 == 0:
        return (quick_exp_mod(x, n//2, mod)**2)%mod
    else:
        return (x * (quick_exp_mod(x, n//2, mod))**2)%mod
    
    return 0


def is_permutation(a, b):
    if len(a) == 0 and len(b) == 0:
        return(True)
    elif len(a) != len(b):
        return(False)
    if a[0] in b:
        return(is_permutation(a[1:], b[:b.index(a[0])]+b[b.index(a[0])+1:]))
    else:
        return(False)
        