def get_num_words(content):
    count = 0
    for word in content.split():
        count += 1
    return count

def get_num_chars(content):
    chars = {}
    content = content.lower()
    
    for char in content:
        chars[char] = chars.get(char, 0) + 1
    
    return chars

def get_report(content):
    
    words = get_num_words(content)
    chars = get_num_chars(content)
    letters = dict_to_list(chars)
    
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in letters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
   
def dict_to_list(content):    
    unsorted_list = []
    
    for char in content:
        unsorted_list.append({"char": char, "num": content[char]})
   
    unsorted_list.sort(reverse=True, key=lambda x: x["num"])
    
    return unsorted_list  
