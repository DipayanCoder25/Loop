decimal_number = int(input("Enter a decimal number: "))

binary_number = ""
number = decimal_number 


while number > 0:
    remainder = number % 2
    binary_number = str(remainder) + binary_number
    number = number // 2

if binary_number == "":
    binary_number = "0"

print(f"Binary of {decimal_number} is {binary_number}")

