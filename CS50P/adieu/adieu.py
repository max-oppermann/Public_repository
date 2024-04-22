import inflect
p = inflect.engine()


# mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# "apple, banana and carrot"

def main():
    list_names = []
    try:
        while True:
            name = input().title()
            list_names.append(name)
    except EOFError:
        pass
    joined_names = p.join((list_names))
    print("Adieu, adieu, to " + joined_names)




'''
def get_names():
    while True:
        try:
            name = input("Name:").title()
            return name
        except EOFError:
            raise
'''
main()
