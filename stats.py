def get_word_count(book_text):
    word_array = book_text.split()
    return len(word_array)

def get_letter_count(book_text):
    lowercase_text = book_text.lower()
    letter_count = {}
    for char in lowercase_text:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def get_letter_count_sorted(book_text):
    letter_count = get_letter_count(book_text)
    sorted_letter_count = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_letter_count