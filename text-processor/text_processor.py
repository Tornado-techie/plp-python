# Step 1: Read from input.txt
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Count words
words = content.split()
word_count = len(words)

# Step 3: Convert text to uppercase
content_upper = content.upper()

# Step 4: Write to output.txt with word count
with open("output.txt", "w") as outfile:
    outfile.write("=== PROCESSED TEXT ===\n")
    outfile.write(content_upper + "\n")
    outfile.write(f"\nWord Count: {word_count}\n")

# Step 5: Print success message
print("✅ Success! 'output.txt' created with processed text and word count.")

