with open("story.txt", "r") as f:
    story = f.read()

# print(story)

target_start = "<"
target_end = ">"

start_of_word = -1

words = set()

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        words.add(story[start_of_word: i + 1])

print(words)

# dict = {}

for word in words:
    userInput = input(f"Enter a word for {word} : ")
    story = story.replace(word, userInput)
    # dict[word] = userInput 

# print(dict)
print(story)    