
# Read words from source file
with open("input.txt", "r") as file:
    words = file.read().split()

# Convert words to lowercase
words = [word.lower() for word in words]

# Sort words alphabetically
words.sort()

# Write words into destination file
with open("output.txt", "w") as file:
    for word in words:
        file.write(word + "\n")

# Print confirmation message
print("Words sorted and saved successfully!")
