def main():
    book_contents = get_book_contents('frankenstein.txt')
    generate_output(book_contents)

def word_count(string):
    wordList = string.split()
    return len(wordList)

def char_appearance(string):
    characterList = list(string)
    charApp = {}
    for char in characterList:
        sanitized_char = char.lower()
        if sanitized_char in charApp and sanitized_char.isalpha():
            charApp[sanitized_char] += 1
        elif sanitized_char not in charApp and sanitized_char.isalpha():
            charApp[sanitized_char] = 1
    return charApp

def convert_dict_to_list(dict):
    temp_list = []
    for item in dict:
        temp_list.append({"character": item, "num": dict[item]})
    temp_list.sort(reverse=True, key=sort_dict)
    return temp_list

def sort_dict(dict):
    return dict["num"]

def get_book_contents(book):
    with open(f"books/{book}") as f:
       return f.read()

def generate_output(book_contents):
    book_word_count = word_count(book_contents)
    character_appearance = char_appearance(book_contents)
    formatted_dictionary = convert_dict_to_list(character_appearance)

    print('--- Welcome to word count usa --')
    print(f"{book_word_count} words found in the document")

    for item in formatted_dictionary:
        print(f"The {item['character']} character was found {item['num']} times")

    print("-- Thanks for visiting word count usa --")

main()
