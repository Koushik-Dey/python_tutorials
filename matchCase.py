x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("x is 0")
    case 4:
        print("x is 4")
    case _ if (x != 90):
        print(x, "x is not 90")
