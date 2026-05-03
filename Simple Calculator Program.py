x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))
z = (input("Enter your operator(+,-,*,/,%): ").strip())


if z == "+":
    print("The result is:", (x+y))
elif z == "-":
    print("The result is:", (x-y))
elif z == "*" :
    print("The result is:", (x*y))
elif z == "/" :
    if y == 0:
        print("errror: div by 0 not allowed")
    else:
        print("The result is:", (x/y))
elif z == "%" :
    if y == 0:
        print("errror: div by 0 not allowed")
    else:
        print("The result is:", (x%y))
else:
    print("Invalid operator")
exit()
