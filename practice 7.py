'''Create a program that computes for the BMI of a person'''

'''Input -> weight, height
bmi = 703 * weight/(height * height)'''

w = eval(input("Enter weight(kg): "))
h = eval(input("Enter height(m): "))

bmi =(w / (h * h))

print (bmi)