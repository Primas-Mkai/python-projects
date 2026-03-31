def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Select operation \n"
      "1. +\n"
      "2. -\n"
      "3. *\n" 
      "4. /\n")

sel = int(input("select(1 - 4): "))

if sel == 1:
    print(add(num1, num2))
elif sel == 2:
    print(sub(num1, num2))
elif sel == 3:
    print(multiply(num1, num2))
elif sel == 4:
    print(divide(num1, num2))
else:
    print("Inalid input")
