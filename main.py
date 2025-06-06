from stats import count_words, count_char

def get_book_text(book):
    
    with open(book) as b: 
      book_content = b.read()
      return book_content

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_of_words = count_words(book_text)
    num_of_char = count_char(book_text)
    print(f"{num_of_words} words found in the document")
    print(num_of_char)
    
main()


