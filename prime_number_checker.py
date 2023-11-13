def prime_checker(number):
    divisor = number - 1
    div_list = []
    is_prime = 0
    
    while divisor > 1:
        check_div = (number % divisor)
        #print(check_div)
        div_list.append(check_div)
        divisor -= 1
    if is_prime in div_list:
        print("Not a prime number")
    else:
        print("It's a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)