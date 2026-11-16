import math

print("""SCIENTIFIC CALCULATOR
______________________
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Square
6.Squareroot
7.Logarithm
8.Sine
9.Cosine
10.Tangent""")

choice=int(input("Enter Your Choice:"))

match choice:
    
    case 1:
        a=float(input("Enter First Number"))
        b=float(input("Enter Second Number"))
        print(f"Answer={a+b}")
        
    case 2:
        a=float(input("Enter First Number"))
        b=float(input("Enter Second Number"))
        print(f"Answer={a-b}")
        
    case 3:
        a=float(input("Enter First Number"))
        b=float(input("Enter Second Number"))
        print(f"Answer={a*b}")    
        
    case 4:
        a=float(input("Enter First Number"))
        b=float(input("Enter Second Number"))
        print(f"Answer={a/b}")
             
    case 5:
        a=float(input("Enter Number"))
        print(f"Answer={a*a}")
        
    case 6:
        a=float(input("Enter Number"))
        print(f"Answer={math.sqrt(a)}") 
        
    case 7:
        a=float(input("Enter Number"))
        print(f"Answer={math.log(a,10)}")
          
    case 8:
        a=float(input("Enter Number"))
        print(f"Answer={round(math.sin(math.radians(a)),2)}") 
        
    case 9:
        a=float(input("Enter Number"))
        print(f"Answer={round(math.cos(math.radians(a)),2)}") 
        
    case 10:
        a=float(input("Enter Number"))
        print(f"Answer={round(math.tan(math.radians(a)),2)}")
    case _:
        print("invalid choice :(")              