import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(f):
    file_contents = f.read()
    return file_contents

from stats import (get_num_words,
                   chars_dict_to_sorted_list, 
                   get_num_characters
                   )

def main():
    with open(sys.argv[1]) as f:
         book1 = get_book_text(f)
         book2 = get_num_words(book1)
         book3 = get_num_characters(book1)
         book4 = chars_dict_to_sorted_list(book3)
         print_report(book1, book2, book4)


def print_report(book4, book2, chars_sorted_list):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {book2} total words")
        print("--------- Character Count -------")

        for item in chars_sorted_list:
            if not item["letter"].isalpha():
                continue
            print(f"{item['letter']}: {item['count']}")
        print("============= END ===============")

main()

