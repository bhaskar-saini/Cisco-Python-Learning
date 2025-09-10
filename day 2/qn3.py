sentence = input("Enter Sentence :\n")
words = sentence.split()

upper_words = tuple(word.upper() for word in words)

with open("sentence_data.txt","w") as file:
    file.write("List of words:\n")
    file.write(str(words) + "\n")
    file.write("Tuple of words:\n")
    file.write(str(upper_words) + "\n")

print("Reading:\n")

with open("sentence_data.txt","r") as file:
    data = file.read()
    print(data)