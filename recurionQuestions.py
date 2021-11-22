# find the sum of digits of a positive integer number using recurionQuestions

def sum_digits(n):
    assert n == int(n) and n >= 0, 'Number must be positive integer!'
    if 0 <= n < 10:
        return n
    else:
        return n%10 + sum_digits(n//10)

# Calculate power of number using recurion

def power_of_number(number,power):
    assert power == int(power), 'Power should be integer!'
    
    minus_power = True if power != abs(power) else False
    if power == 0:
        return 1
    else:
        return 1/(number * power_of_number(number, abs(power)-1)) if minus_power else number * power_of_number(number, abs(power-1))


# Find greates common divisor of two numbers using recursion

def GCD(num1, num2):
    # To find gcd of num1 and num2 lets use euclidean algorithm
    # Example: gcd(48,18) 
    # step 1: 48//18 = 2 remainder 12
    # step 1: 18//12 = 1 remainder 6
    # step 1: 12//6 = 2 remainder 0 So 6 is the greates common divisor
    
    assert int(num1) != num1 or int(num2) != num2, 'Numbers should be integers'
    
    remainder = max([abs(num1), abs(num2)])%min([abs(num1), abs(num2)])
    
    if remainder == 0:
        return min([abs(num1), abs(num2)])
    else:
        return GCD(min([abs(num1), abs(num2)]),remainder)
        
        
# Convert number from Decimal to Binary using recursion 

def binary_conversion(num):
    # converting from Decimal to Binary mathematicaly:
    # step 1:  divide the number by 2 
    # step 2: Get the integer quotient for the next iteration 
    # step 3: Get the emainder for the binary digit
    # step 4: Repeat the steps until the quotient is equal to 0
    # 13 to binary: 13//2 = 6 (Remainder: 1) => 6//2 = 3 (Remainder: 0) => 3//2 = 1 => (Remainder: 1) 1//2 = 0 (Remainder: 1)
    # so 13 to binary is 1101
    
    assert num == int(num), 'the parameter can be an integer only!'
    
    if abs(num)//2 == 0:
        return str(abs(num)%2)
    else:
        return binary_conversion(abs(num)//2) + str(abs(num)%2)
    

def productOfArray(arr):
    assert len(arr) != 0, 'arr must not be not empty!'
    
    if len(arr) < 2:
        return arr[0]
    else:
        
        return arr[0] * productOfArray(arr[1:])
    
def reverse(string):
    assert len(string) != 0, 'string must not be empty!'
    
    if len(string) == 1:
        return string
    else:
        return string[-1] + reverse(string[0:-1])
    
