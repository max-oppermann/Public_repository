import validators

mail = input("Mail:")
if validators.email(mail):
    print("Valid")
else: print("Invalid")

