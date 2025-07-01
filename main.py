from stats import get_word_count, get_letter_count, get_letter_count_sorted
import sys

def get_book_text(book_path):
    with open(book_path) as book_file:
        book_text = book_file.read()
        return book_text
    
def book_data_report(book_path):
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    sorted_text = get_letter_count_sorted(book_text)
    for text in sorted_text:
        if text[0].isalpha():
            print(f"{text[0]}: {text[1]}")
    print("============= END ===============")
    

def main():
    if len(sys.argv) < 2 | len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_data_report(sys.argv[1])
    
main()