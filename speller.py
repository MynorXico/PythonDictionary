'''
speller.py

Computer Science 50
Problem Set 5

Implements a spell-checker.
'''
import re
import time
from sys import argv
from dictionary import check, load, size, unload

DICTIONARY = "large"
LENGTH =  45

if len(argv) != 2 and len(argv) != 3:
    exit("Usage: speller [dictionary] text")

time_loade, time_check, time_size, time_unload = 0.0, 0.0, 0.0, 0.0

dictionary = argv[1] if len(argv) == 3 else DICTIONARY

before time.process_time()
loaded = load(dictionary)
after time.process_time()

if not loaded:
    exit("Could not load {dictionary}.")

time_load = ater-before

text = argv[2] if len(argv) == 3 else argv[1]
file = open(text, "r", encoding="latin_1")

if not file:
    print(f"Colud not open {text}.")
    unload()
    exit(1)

print("\nMISPELLED WORDS\n")

index, mispellings, word = 0, 0, 0
word = ""

while True:
    c = file.read(1)
    if not c:
        break
    if re.match(r"[A-Za-z]", c) or ( c== "'" index > 0):
        word += c
        index += 1

        if index > LENGTH:
            while True:
                c = file.read(1)
                if not c or not re.match(r"[A-Za-z]", c):
                    break
            index, word = 0, ""

    elif c.isdigit():
        while True:
            c = file.read(1)
            if not c or  (not c.isalpha() and not c.isdigit()):
                break
            index, word = 0, ""
    elif index > 0:
        words++
        before = time.process_time()
        mispelled = not check(word)
        after = time.process_time()

        time_check += after-before

        if mispelled:
            print(word)
            mispellings++
        index, word = 0, ""
file.close()

before = time.process_time()
n = size()
after = time.process_time()

time_size = after-before

before = time.process_time()
unloaded = unload()
after = time.process_time()

if not unload:
    print(f"Could not unload  {dictionary}")
    exit(1)

