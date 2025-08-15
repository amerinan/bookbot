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

    for item in content:
        print(f"{item['char']}: {item['num']}")
   
def dict_to_list(content):    
    unsorted_list = []
    
    for char in content:
        unsorted_list.append({"char": char, "num": content[char]})
    unsorted_list.sort(reverse=True, key=lambda x: x["num"])
    
    return unsorted_list  
