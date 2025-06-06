def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_char(book_text):

    char_count = {}
    characters = book_text.lower()

    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count