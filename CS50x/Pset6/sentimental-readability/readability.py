
from cs50 import get_string


def main():
    text = get_string("text: ")
    num_words = len(text.split())
    num_letters = 0
    num_sentences = 0

    for c in text:
        if c in [".", "!", "?"]:
            num_sentences += 1
        if c.isalpha():
            num_letters += 1

    grade = round(0.0588 * (num_letters / num_words * 100) - 0.296 * (num_sentences / num_words * 100) - 15.8)
    if grade >= 1 and grade < 16:
        print(f"Grade {grade}")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print("Grade 16+")


main()
