from collections import Counter

# Take paragraph input
paragraph = input("Enter a paragraph:\n")

# Total characters
total_characters = len(paragraph)

# Total words
total_words = len(paragraph.split())

# Total sentences (. ! ?)
total_sentences = sum(paragraph.count(mark) for mark in ".!?")

# Most frequent character (excluding spaces)
characters = [char for char in paragraph if char != " "]
if characters:
    most_frequent = Counter(characters).most_common(1)[0]
    most_char = most_frequent[0]
    frequency = most_frequent[1]
else:
    most_char = None
    frequency = 0

# Uppercase and lowercase letters
uppercase = sum(1 for char in paragraph if char.isupper())
lowercase = sum(1 for char in paragraph if char.islower())

# Display results
print("\nString Statistics")
print("-----------------")
print("Total characters:", total_characters)
print("Total words:", total_words)
print("Total sentences:", total_sentences)

if most_char:
    print(f"Most frequent character: '{most_char}' ({frequency} times)")
else:
    print("Most frequent character: None")

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)