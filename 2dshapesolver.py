x = 1
p = 3.14
while x != "STOP" or "stop":
    x = str(input("TYPE 'T' FOR TRIANGLE, 'C' FOR CIRCLE AND 'R' FOR RECTANGLE. 'STOP' TO END CODE "))
    if x == "STOP":
        break
    elif x == "T" or x == "t":
        b = float(input("Base: "))
        h = float(input("Height: "))

        print("Area = ", (b*h)/2)
    elif x == "R" or x == "r":
        l = float(input("length: "))
        w = float(input("width: "))

        print("Area = ", l*w)
        print("Perimeter = ", 2*l + 2*w)
    elif x == "C" or x == "c":
        r = float(input("radius: "))
        s = str(input("Is it a sector? Y or N?"))
        if s == "Y" or s == "y":
            a = float(input("degrees: "))
            print("sector perimeter = ", 2*r + 2*r*p*(a/360))
            print("sector area = ", r**2*p*(a/360))
        elif s == "N" or s == "n":
            print("circumference = ", 2*r*p)
            print("area = ", r**2*p)
    else:
        print("bad input :(")







