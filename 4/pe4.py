# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers

def products():
    products = []
    for i in range(100, 1000):
        for j in range(100, 1000):       
            products.append(i * j)
    return products

def is_palidrome(n):
    divisor = 1
    while (n / divisor >= 10): 
        divisor *= 10
  
    while (n != 0): 
        head = n // divisor  
        tail = n % 10

        if (head != tail):  
            return False
    
        n = (n % divisor)//10
        divisor = divisor/100
          
    return True

def palindromes(list):
    palindromes = []
    for i in products:
        if (is_palidrome(i)):
            palindromes.append(i)
    return max(list)

products = products()
max_palindrome = palindromes(products)
print(max_palindrome)
