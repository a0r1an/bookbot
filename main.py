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
    try:
        with open(f"books/{book}") as f:
            return f.read()
    except FileNotFoundError:
        print("Oh no! We couldnt find this book. Try running this program again and looking for a different book.")
        print("You can also try to see if you mispelled the book name.")
        return None

def main():
    print('--- Welcome to word count usa --')
    user_name = input("What is your name rider? ")
    print(f"Well, Hello {user_name}, we hope to provide you with the best word counting experience")
    book_name = input("Can you please provide me with the book you want to word count? ")
    book_contents = get_book_contents(f"{book_name.lower()}.txt")
    if book_contents == None:
        return
    book_word_count = word_count(book_contents)
    character_appearance = char_appearance(book_contents)
    formatted_dictionary = convert_dict_to_list(character_appearance)
    print(f"{book_word_count} words found in the document")
    print("We also have the ability to give you data on how often specific characters were used...")
    should_character_count= input("Would you like to see that? ")
    sanitize_answer = should_character_count.lower().strip()
    yes_answers = ['yes', 'yup', 'yep', 'ya', 'y', 'sure', 'si', 'ja']
    if sanitize_answer in yes_answers:
        for item in formatted_dictionary:
            print(f"The {item['character']} character was found {item['num']} times")
    else:
        print("No problem")
    print("-- Thanks for visiting word count usa --")

main()
