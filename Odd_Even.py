a=input("Enter a number: ")
a=int(a)

if a%2 == 0:
    print(a, "is an even number.")
elif (a%2) > 0:
    print(a, "is an odd number.")
else:
    print(a, "is not an even number.")