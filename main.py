import sys
from stats import get_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    sys.argv
    
        
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book = get_book_text(sys.argv[1])
    get_report(book)
    
main()
