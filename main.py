import sys
from stats import get_book_text
from stats import get_word_count
from stats import get_character_count
from stats import proper_list_printing


#####################

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        word_count = get_word_count(text)
        character_count = get_character_count(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        proper_list_printing(character_count)
        print("============= END ===============")

main()