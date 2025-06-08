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




def sort_on(dict):
    return dict["num"]

def sort_list(characters_values):
    sorted_list = []
    for character, character_count in characters_values.items():
        if character.isalpha() == True:
            sorted_list.append({"char" : character, "num" : character_count})
            sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list