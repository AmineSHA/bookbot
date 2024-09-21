
def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    book = "books/frankenstein.txt"
    
    generate_report(book,alphabet)


    
def read_file(path_to_file):
    text=''
    with open(path_to_file) as f:
        text = f.read()
    return text

def get_word_count(text):
    words = text.split()
    return len(words)

def count_characters(text, characters_of_interest):
    
    character_count = {}
    
    for c in text.lower():
        if c in characters_of_interest:
           if c in character_count:
               character_count[c] += 1 
           else:
               character_count[c] = 1
    
    character_count_sorted =   {char: count for char, count in sorted(character_count.items(), key=lambda char: char[1], reverse=True)}
    
    return character_count_sorted

def print_character_count(character_count):
    for char in character_count:
        print(f"{char} appeared {character_count[char]} times.")
        print("---")

def generate_report(file_name, chars_of_interest):
    text = read_file(file_name)
    word_count = get_word_count(text)
    character_count = count_characters(text, chars_of_interest)

    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document.")
    print('\n')

    for char in character_count:
        print(f" The {char} character was found {character_count[char]} times.")

    print('--- End report ---')
    
main()