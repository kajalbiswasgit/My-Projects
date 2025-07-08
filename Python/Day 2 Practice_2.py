# Ask the user for their name and greet them.
name= input("What is your name: ")
print ("Hello " + name + " welcome to python")

#Ask the user for their favorite hobby and print a sentence using it.
name= input("What is your name?: ")
hobby= input("What is your favourite hobby? : ")
print (name , "favourite hobby is to",hobby)

# Create a script that prints your name, age, and city using print().
name= input ("your name: ")
age= input ("what is your age: ")
city= input ("your city name: ")
print (name, "is ",age, " and he lives in",city )

# Ask the user for two numbers and show their addition, subtraction, and multiplication.
num1= int(input("Please enter the first number: ") )
num2= int(input("Please enter the second number: ") )
print ("The addition is: ", num1+num2)
print ("The substraction is: ", num1-num2)
print ("The multiplication is: ", num1*num2)
print ("The dividation is: ", num1/num2) 

#Ask the user to enter a number. If it’s not a number, show a custom error message
try:
    num1= int (input ("Please enter the first no: "))
    num2= int (input ("Please enter the second no: "))
    print("You entered: ", num1)
except ValueError:
    print("Error: Please enter a valid numeric digit")