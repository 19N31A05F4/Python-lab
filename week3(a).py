num1 =eval(input("Enter the first number:"))
num2 =eval(input("Enter the second number:"))

def perform(num1,num2):
    while 1:
        print("**********")
        print("1.To perform addition")
        print("2.To perform subtraction")
        print("3.To perform multiplication")
        print("4.To perform division")
        print("5.To exit")
        ch=int(input())
        if ch==1:
            c=num1+num2
            print("Addition of",num1,"and",num2,"is:",c)
        elif ch==2:
            c=num1-num2
            print("Subtraction of",num1,"and",num2,"is:",c)
        elif ch==3:
            c=num1*num2
            print("Multiplication of",num1,"and",num2,"is:",c)
        elif ch==4:
            c=num1/num2
            print("division of",num1,"and",num2,"is:",c)
        elif ch==5:
            exit()
        else:
            print("Enter a number from the menu!")

perform(num1,num2)