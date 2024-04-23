# camel.py
i = input("camelCase: ")

for l in i:
    if l.isupper():
        print("_"+l.lower(), end ='')
    else:
        print(l, end ='')
