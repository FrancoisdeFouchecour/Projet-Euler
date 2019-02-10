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


def phi(n):
    value = 1
    decompo = prime_decomposition_normalise(prime_decomposition(n))
    for mult, exp in decompo:
        value *= (mult - 1)*mult**(exp - 1)
    return value
        

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


def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]



def min_factor(n):
    factor = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if factor[i] == i:
            tmp =  -1 + (n - n%i)//i
            
            factor[2*i::i] = [i]*tmp
    return factor


def v_p(n, p):
    count = 1
    factor = p
    while n%factor == 0:
        count += 1
        factor *=p
    return count - 1
    

def new_decmpo(n):
    d = 2
    factor = []
    while d*d <= n:
        if n%d == 0:
            k = v_p(n, d)
            factor.append((d, k))
            n = n//(d**k)
        d += 1
    if n != 1:
        factor.append((n, 1))
    return factor
        
    