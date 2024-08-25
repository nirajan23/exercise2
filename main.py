
# Write a program that asks your name and then greets you by your name: Examples:

name = input("Enter your name = ")
print("Hello," + name + "!")


# 2.Write a program that asks the user for the radius of a circle and the prints out the area of the circle.


r = float(input("Enter radius of the circle = "))
π = 3.14
area = π*r*r

print("area of the circle = " + str(area) + ".")

#  3 Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.


length = int(input(" Enter length of the rectangle = "))
width = int(input(" Enter width of rectangle ="))

perimeter = 2*(length+width)
area1 = length*width


print("Perimeter of rectangle = " + str(perimeter))
print("Perimeter of rectangle = " + str(area1))

# 4. Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
print("Enter three integer number")

vars_a = int(input("a = "))
vars_b = int(input("b = "))
vars_c = int(input("c = "))

sum = (vars_a+vars_b+vars_c)
product = (vars_a*vars_b*vars_c)
average = (vars_a+vars_b+vars_c)/3

print("sum of a,b & c = " + str(sum))
print("product of a,b & c = " + str(product))
print("average of a,b & c = " + str(average))

 # 5. Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
print("give mass in talents, pounds and lots.")



talents = float(input("First give talents = "))
pounds = float(input("First give pound = "))
lots = float(input("First give lots = "))

lotsInGrams =13.3
poundsIngrams = 32 * lotsInGrams
talentInGrams = 20 * poundsIngrams

mass = talents * talentInGrams + pounds * poundsIngrams + lots * lotsInGrams
kg = int(mass//1000)
grams = mass % 1000

print(f"The weight in modern units: ")
print(f"{kg} kilograms and {grams:.2f} grams.")



# 6.Write a program that draws two random combinations of numbers for a combination lock

from random import randint

num1 = randint(0, 9)
num2 = randint(0, 9)
num3 = randint(0, 9)

print (f"code 1 : {num1}{num2}{num3}")

num4 = randint(1, 6)
num5 = randint(1, 6)
num6 = randint(1, 6)
num7 = randint(1, 6)


print (f"code 2 : {num4}{num5}{num6}{num7}")
