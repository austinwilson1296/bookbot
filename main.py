def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = letter_count(text)
    dict_sort = sort_dict(num_letters)
    print(f'----Begin report of {book_path}----')
    print(f'{num_words} words found in the document')
    for item in dict_sort:
        for key,value in item.items():
            print("\n")
            print(f'The {key} character was found {value} times')  
    print("---end report---")  


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def letter_count(text):
    letter_dict = {}
    lower_string = text.lower()
    for letter in lower_string:
        if letter in letter_dict:
            letter_dict[letter] = letter_dict[letter] + 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    return dict["key"]

def sort_dict(letters):
    dict_list = []
    for key,value in letters.items():
        if key.isalpha():
            dict_list.append({key:value})
    sorted_list = sorted(dict_list,reverse=True,key=lambda x: list(x.values())[0])
    return sorted_list
    


main()