file = open("input_text.txt", "r")

words = file.read().split()
file.close()
vowels = ["a", "e", "i", "o", "u"]
new_words = []
for word in words:
    if word[0].lower() in vowels:
        new_words.append(word + "way")
    else:
        word_slice = ""
        for letter in word:
            if letter.lower() in vowels:
                new_words.append(word[len(word_slice) :] + word_slice + "ay")
                break
            else:
                word_slice += letter

open("output_text.txt", "w").write(" ".join(new_words))
