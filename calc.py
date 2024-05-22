def add (num1, num2):
    return num1 + num2
def subtract (num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
def divide (num1, num2):
    return  num1 / num2
def modulus (num1, num2):
    return num1 % num2
def exponentiation (num1, num2):
    return num1 ** num2
def floordivision (num1, num2):
    return num1 // num2

print("Please select operation -\n" \
  "1.Add\n"\
  "2.Subtract\n"\
  "3.Multiply\n"\
  "4.Divide\n"\
  "5.Modulus\n"\
  "6.Exponentiation\n"\
  "7.Floor Division\n")         

select =int(input("select operations form 1,2,3,4,5,6,7:"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
 
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
 
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
 
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))

elif select == 5:
    print(number_1, "%", number_2, "=",
                    modulus(number_1, number_2))    

elif select == 6:
    print(number_1, "**", number_2, "=",
                    exponentiation(number_1, number_2))      

elif select == 7:
    print(number_1, "//", number_2, "=",
                    floordivision(number_1, number_2))                                            
else:
    print("Invalid input")