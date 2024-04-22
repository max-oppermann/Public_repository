# interpreter.py
one, operator, two = input("Expression: ").split(" ")
if operator == "+":
    print(round(float(one) + float(two), 1))
elif operator == "-":
    print(round(float(one) - float(two), 1))
elif operator == "*":
    print(round(float(one) * float(two), 1))
elif operator == "/":
    print(round(float(one) / float(two), 1))
