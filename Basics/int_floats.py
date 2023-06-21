# <======Integers and Floats -------->

num1=3
num2=3.14
print(type(num1))
print(type(num2))
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

print(3+2)
print(3-2)
print(3*2)
print(3/2)  #return 1.5 
print(3//2) #return 1
print(3**2)
print(3%2)

#abs( ) which return the number after removing the -ve sign
print(abs(-25))
#round()
print(round(3.147,1))

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

#------Retuen True or False
print(3 == 2)
print(3 != 2)
print(3 > 2)
print(3 < 2)
print(3 >= 2)
print(3 <= 2)

#Casting 
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)