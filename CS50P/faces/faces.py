def main():
    faces = convert(input("Tell me something :)"))
    print(faces)

def convert(text):
    return text.replace(':)', '🙂').replace(':(', '🙁')

main()
