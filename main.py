from stats import get_num_words, get_num_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    content = get_book_text("books/frankenstein.txt")
    
    get_num_words(content)
    print(get_num_chars(content))
    
main()
