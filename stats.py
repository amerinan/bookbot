def get_num_words(content):
    count = 0
    for word in content.split():
        count += 1
    print(f"{count} words found in the document")

def get_num_chars(content):
    chars = {}
    content.lower()
    
    for char in content:
        chars[char] = chars.get(char, 0) + 1
    
    return chars