def get_num_words(content):
    count = 0
    for word in content.split():
        count += 1
    print(f"{count} words found in the document")

