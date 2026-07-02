a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a > b and a > c:
    print("Greatest Number =", a)
elif b > c:
    print("Greatest Number =", b)
else:
    print("Greatest Number =", c)