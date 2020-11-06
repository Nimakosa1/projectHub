"""1. This simple program finds the count
of digits present in an integral number and lists
the digits present.
"""

num_int = int(input("Enter the integral number: "))
count = 0
digits_lst = list()

while num_int != 0:
    digit = num_int % 10
    digits_lst.append(str(digit))
    num_int = num_int // 10
    count += 1

digits_lst.reverse()
string = ", ".join(digits_lst)
print("The number of digits in the number is", count, "and the digits are", string)


"""2. The program below checks whether a given number is
prime or not
"""

num_str = input('Enter the number: ')
num_int = int(num_str)

if num_int > 1:
    for i in range(2, num_int):
        if (num_int % i) == 0:
            print(num_int,"is not a prime number")
            break
    else:
        print(num_int, "is a prime number")
else:
    print(num_int,"is not a prime number")


"""3. The simple program below utilizes a function that takes in as input temperature in
Celsius and converts it to temperature in Fahrenheit.
"""

def celsius_to_fahrenheit(temp_celsius):
    return (9/5)*temp_celsius + 32

celsius = float(input("Enter the temperature in celsius: "))
Fahrenheit = celsius_to_fahrenheit(celsius)
print("The temperature equivalent of", celsius,"degrees celsius is {:.2f} degrees Fahrenheit".format(Fahrenheit))


"""4. The program here makes use of two functions to find the number of digits
present in the factorial of an integer.
"""

def factorial(n):
    """The function (recursive) takes an integer n as input, calculates its factorial
    and returns the value calculated.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def count_digits(num_int):
    """This function takes as input an integer and determines the number of
    digits present in the number.
    """
    count = 0

    while num_int != 0:
        num_int = num_int // 10
        count += 1

    return count

num = int(input("Enter the number: "))
num_digits = count_digits(factorial(num))
print("The number of digits in the factorial of {} is {}".format(num, num_digits))


"""5. Program that determines the number of stones one has which are
jewels by matching a pair of strings.
"""

S = input("Enter the string representing stones you have: ")
J = input("Enter the string representing the types of stones that are jewels: ")
count = 0

for char_j in J:
    for char_S in S:
        if char_j == char_S:
            count += 1

print("Output: ",count)
