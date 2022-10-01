from Task_1_1 import sum_of, factor

print("To know the sum of the 2 numbers please do next steps >>>")
a, b = int(input("Enter first number: ")), int(input("Enter second number: "))
print(f"The sum of 2 numbers is: {sum_of(a, b)}")


fact = int(input("Please enter a number: "))
print(f"Factorial of {fact}: is {factor(fact)}")
