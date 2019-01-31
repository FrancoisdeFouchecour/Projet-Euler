def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def is_prime(n):
    #return first prime factor if composite, return itself otherwhise (and -1 if n < 0)
    if n < 1:
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


def prime_decomposition_normalise(decompostion):
    #reformat prime decomposition
    unique_decomposition = []
    for num in decompostion:
        if unique_decomposition.count(num) == 0:
            unique_decomposition.append(num)
    
    return([(num, decompostion.count(num))for num in unique_decomposition])
        

def ppcm_multiple(tab_number):
    #return the ppcm of all numbers in tab
    tab_decomposition = [prime_decomposition_normalise(prime_decomposition(num)) for num in tab_number]
    ppcm_decomposition = []
    
    for decomposition in tab_decomposition:
        for (div, exp) in decomposition:
            if exp > ppcm_decomposition.count(div):
                for i in range(exp-ppcm_decomposition.count(div)):
                    ppcm_decomposition.append(div)
                    
    ppcm_decomposition.sort()
    return ppcm_decomposition


def sum_of_divisors(number):
    result = 1
    if number == 1:
        return 1
        
    decomposition = prime_decomposition_normalise(prime_decomposition(number))
    
    for num, exp in decomposition:
        result *= (num**(exp + 1) - 1)//(num - 1)
    return result
        