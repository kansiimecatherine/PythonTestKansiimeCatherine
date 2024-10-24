# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.

def number():
    total = 0 
    while True:
        number_entered = float(input("Enter number 0 to stop:  "))
        if number_entered ==0:
            break
        total += number_entered
        print(f"The sum of the number is: {total}")
number()
        



# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2
number = 1
while number <= 100:
    range(1,101)
    if number % 2 != 0:
        print(number)
        number+=1





