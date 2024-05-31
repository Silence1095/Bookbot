def main():
    with open('books/frankenstein.txt') as book:
        file_contents = book.read()
        count_words(file_contents)
        char_list = to_list(count_char(file_contents))
        char_list.sort(reverse=True, key=sort_on)
        print_char(char_list)

def count_words(book):
    words = book.split()
    print(len(words))

def count_char(book):
    lowered = book.lower()
    count = {}
    for i in lowered:
        if i not in count and i.isalpha():
            count[i] = 0
        if i in count and i.isalpha():
            count [i] += 1
        else:
            pass
    return count

def to_list(dict):
    dict_list = []
    for i in dict:
        dict_list.append({'char':i, 'num': dict[i]})
    return dict_list

def sort_on(dict):
    return dict['num']

def print_char(list):
    for i in list:
        print(f"The '{i['char']}' character was found {i['num']} times")

main()