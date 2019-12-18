"""
For the numbers 1-100.  If the number is divisible by 3 print the word Fizz.  
If the number is divisible by 5   print the word Buzz.  
If the number is divisible by both 3 and 5 print Fizz Buzz.  Otherwise print the number.
"""
for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print('Fizz Buzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
