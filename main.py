from stats import get_num_words, get_num_chars, get_report, dict_to_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    content = get_book_text("books/frankenstein.txt")
    
    words = get_num_words(content)
    chars = get_num_chars(content)
    
    get_report(dict_to_list(chars))
    
main()
