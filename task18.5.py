wordlist = list()

with open("churchill_speech.db", "r") as speech:
    for word in speech.read().split(): wordlist.append(word.strip('.,!:?"').lower())
uniquewords = dict()
for word in wordlist:
    if word in uniquewords: uniquewords[word] += 1
    else: uniquewords[word] = 1
orderedwords = list()
for word in uniquewords: orderedwords.append((uniquewords[word], word))

while True:
    if input("option (top words/check word)> ") == "top words":
        print("Here are the top 10 most common words:")
        for occurences,word in sorted(orderedwords, reverse=True)[0:9]: print(f"'{word}' appeared in the text {occurences} times")
    else:
        pickedword = input("word to check> ")
        if pickedword in uniquewords: print(f"'{pickedword}' appeared {uniquewords[pickedword]} times!")
        else: print("Sorry - that word didn't appear in the text")
