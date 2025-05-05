print("Basic Calculator")


num1=float(input("Enter the first number: "))
oper=input("Enter one operation(+,-,*,/) : ")
num2=float(input("Enter the second number:"))

if oper == "+":
    print("Result:",num1 + num2)
elif oper == "-":
    print("Result:", num1 - num2)
elif oper == "*":
    print("Result:", num1 * num2)
elif oper == "/":
    if num2 != 0:
        print("Resultat:", num1 / num2)
    else:
        print("Division by 0 impossible.")
else:
    print("Invalide Operation")