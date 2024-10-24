# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
x1 = int(input("Enter x1:  "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
import math
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between two coordinates is : {distance}") 







# Question 1(ii)
# Write a Python program to find maximum between three numbers.

number_one = int(input("\nEnter the first number:  "))
number_two = int(input("Enter the second number:  "))
number_three = int(input("Enter the third number:  "))
maximum_number = max(number_one,number_two,number_three)
print(f"The maximum number between three the numbers is:{maximum_number}"'\n\n')




