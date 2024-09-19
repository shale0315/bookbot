import string

def main():
    book = get_book()
    # print(book)
    num_words = count_words(book)
    # print(f"Word Count: {num_words}")
    letter_count = count_letters(book)
    # print(letter_count)
    sorted_dictionary_list = convert_dictionary(letter_count)
    sorted_dictionary_list.sort(reverse=True, key=sort_on)
    # print(sorted_dictionary_list)
    report(num_words,sorted_dictionary_list)

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

#Convert Dictionary to List of Dictionaries
def convert_dictionary(dictionary):
    unsorted_dictionary_list = []
    for key in dictionary:
        unsorted_dictionary_list.append({key:dictionary[key]})
    return unsorted_dictionary_list

def sort_on(dict):
    for key in dict:
        return dict[key],key

def report(word_count,sorted_list):
    print(f"--- Begin report of frankenstein.txt ---")
    print(f"Word Count: {word_count}\n")
    for item in sorted_list:
        for key in item:
            print(f"The '{key} character was found {item[key]} times")
    print(" --- End of report ---")

main()