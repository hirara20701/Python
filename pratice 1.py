'''
num1 = 20
num2 = 30
    product <= 1000
        return product
    else
        return num1+num2
'''

def xyz(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1+num2

result = xyz(20,30)
print("The Answer is ", result)

result = xyz(40,30)
print("The Answer is ", result)

