import string

def main():
    book = get_book()
    print(book)
    num_words = count_words(book)
    print(f"Word Count: {num_words}")
    letter_count = count_letters(book)
    print(letter_count)

def get_book():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(text):
    num_words = 0
    words = text.split()
    for word in words:
        num_words += 1
    return num_words

def count_letters(text):
    letter_dict = {}
    alphabet = list(string.ascii_letters)
    for letter in text.lower():
        if letter in alphabet and letter not in letter_dict:
            letter_dict[letter] = 1
        elif letter in alphabet and letter in letter_dict:
            letter_dict[letter] += 1
    return letter_dict

main()