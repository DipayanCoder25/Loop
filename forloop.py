num = float(input("Enter a  number: "))
power = int(input("Enter the power of  "))

result = 1

for i in range(power):
    result *= num

print(f"{num} raised to the power of {power} is: {result}")
