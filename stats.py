def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
        


def get_word_count(book_string):
    words = book_string.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def get_character_count(book_string):
    fixed_text = book_string.lower()
    character_dictionary = {}
    sorted_character_count = []


    for character in fixed_text:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    for letter in character_dictionary:
        if letter.isalpha():
            sorted_character_count.append({"char": letter, "num": character_dictionary[letter]})
            sorted_character_count.sort(reverse=True, key=sort_on)


    return sorted_character_count

def proper_list_printing(character_count_list):
    
    for i in range(0, len(character_count_list)):
        print(f"{character_count_list[i]["char"]}: {character_count_list[i]["num"]}")
        

    return