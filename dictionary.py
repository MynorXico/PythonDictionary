words = set()

def check(word):
    return word.lower() in words

    
def load(dictionary):
    with open(dictionary, "r") as file:
        for line in file:
            # Store word in some data structure
            words.add(line.rstrip("\n"))
            pass
    return True


def size():
    return len(words)

def unload():
    return True
