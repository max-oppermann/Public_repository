def main():
    grocery_list = {}
    try:
        while True:
            item = input().upper()
            if item not in grocery_list:
                grocery_list[item] = 1
            elif item in grocery_list:
                grocery_list[item] += 1
    except EOFError:
        pass
    sorted_list = sorted(grocery_list.keys())

    for i in sorted_list:
        print(grocery_list[i], i)

main()
