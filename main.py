def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import (get_num_words,
                   chars_dict_to_sorted_list, 
                   get_num_characters
                   )

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_characters)
    print_report(book_path, num_words, chars_sorted_list)



def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["letter"].isalpha():
            continue
        print(f"{item['letter']}: {item['count']}")

    print("============= END ===============")


main()

