import sys
from stats import count_words, count_char, sort_list

def get_book_text(book):
    
    with open(book) as b: 
      book_content = b.read()
      return book_content

def main():

    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)          
    else:
        book_location = sys.argv[1]
        book_text = get_book_text(book_location)
        num_of_words = count_words(book_text)
        num_of_char = count_char(book_text)
        sorted_list = sort_list(num_of_char)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at ...{book_location}")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")

        for dic in sorted_list:
            print(f"{dic['char']}: {dic['num']}")

        print("============= END ===============") 

main()


