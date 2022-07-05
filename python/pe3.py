# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math

def prime_factor(n):

    list = []
    while(n % 2 == 0):
        n = n / 2
        n = int(n) 
        list.append(2)

    for i in range(3, int(math.sqrt(n))+1,2):
        while n % i== 0: 
            i = int(i) 
            list.append(i)
            n = n / i 

    if (n > 2):
        n = int(n) 
        list.append(n)

    print(max(list))


prime_factor(600851475143)
