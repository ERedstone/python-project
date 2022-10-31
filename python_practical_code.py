print("Basic Calculator")

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
x = input("[*] for multiplication, [+] for addition, [-] for subtraction: ")

if x == ("+"):
    sum = float(number1) + float(number2)
    print("answer is ", sum)

elif x == ("*"):
    sum = float(number1) * float(number2)
    print("answer is ", sum)

elif x == ("-"):
    sum = float(number1) - float(number2)
    print("answer is ", sum)
else:
 print("invalid input")

e = input("press any key to exit")