def is_prime(n):
    #return first prime factor if composite, return itself otherwhise
    if n == 1:
        return 1
        
    d = 2
    while d*d <= n:
        if n%d == 0:
            return d
        d += 1
    return n


def prime_decomposition(n):
    #return list of prime factor
    factor = is_prime(n)
    
    if(factor == n):
        return([n])
    else:
        return([factor]+prime_decomposition(int(n/factor)))
        