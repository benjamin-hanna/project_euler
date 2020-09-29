# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_integer(x, y):
    if(y == 0):
        exit()
    else: 
        print(x / y)
        smallest_integer(x, (y - 1))


def smallest_mod_through_20_iter():
    guess = 1
    iteration = 20
    
    while (guess > 0):
        print("\r" + str(guess), end="")
        while(guess % iteration == 0):
            if(iteration == 1):
                print("result: ", guess)
                exit()
            iteration = iteration - 1

        iteration = 20
        guess = guess + 1

def product_of_mods():
    mod_list = []

    for i in range(1, 21):
        if(len(mod_list) == 0):
            mod_list.append(i)
        else:
            x = 0 
            for n in mod_list:
                if(i % n == 0):
                    x = (i / n)
                    i = x
            mod_list.append(x)
    
    product = 1
    for n in mod_list:
        product = product * n

    print(product)

if __name__ == "__main__":
    # smallest_integer(232792560, 20)
    # smallest_mod_through_20_iter()
    product_of_mods()


    # 2 / 1 = 2 ; so 1 * 2 
    # 3 / 1 = 3 ; 3 / 2 <- no; 3 * 2
    # 4 / 1 = 4 ; 4 / 2 = 2 <- result is 2

    # not including number itself 
    # 1) if evenly divisible, do the division, get result
    # 2) take the result of the last evenly divisible iteration and multiple by last step

    # from time import sleep
    # for i in range(400):
    #     print("\r" + str(i), end="")
    #     sleep(0.5)
    
    
