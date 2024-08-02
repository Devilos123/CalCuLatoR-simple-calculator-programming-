def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def mulitiplication(x, y):
    return x * y

def division(x, y):
    if x != 0:        
     return x / y
    else:
        return "Error ! Division by zero..."
    


def expoentiation(x, y):
    return x ** y

def modulus(x, y):
    return x % y


print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Expoentiation")
print("6. Modulus")

choice = input("Enter choice (1/2/3/4/5/6): ")

num1 = float(input("first num: "))
num2 = float(input("second num: "))

if choice =='1':
    print("Result: ", addition(num1, num2))
    
elif choice == '2':
    print("Result: ", subtraction(num1, num2))
    
elif choice == '3':
    print("Result: ", mulitiplication(num1, num2))
    
elif choice == '4':
    print("Result: ", division(num1, num2))
    
elif choice == '5':
    print("Result: ", expoentiation(num1, num2))
    
elif choice == '6':
    print("Result: ", modulus(num1, num2))
    
else:
    print("Invalid Input")        
    
    
        
