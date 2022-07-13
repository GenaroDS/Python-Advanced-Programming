# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    file = open(filename, "r")
    words = file.read().replace("\n"," ")    
    words = words.split(" ")
    words = [word.strip(".") for word in words]
    words = [word.strip(",") for word in words]
    print(words)

    return {word : words.count(word) for word in words if words.count(word) >= lower_limit}

