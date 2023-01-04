a = input("Enter value between 5 and 9\n")

if(a == 'quit'):
    print("abhishek")
try:
    a = int(a)
    if(a<5 or a>9):
        print("You entered less than 5 or greater than 9")

except:
    pass
finally:
    pass

