num=str(input("Enter number: "))
mult=1

for i in num:
    mult*=int(i)

print("Multiplication of digits = ", mult)

print("Reversed number: ", num[::-1])

print("Sorted digits: ", sorted(num))

# Output sample:

# Enter number: 1234
# Multiplication of digits =  24
# Reversed number:  4321
# Sorted digits:  ['1', '2', '3', '4']