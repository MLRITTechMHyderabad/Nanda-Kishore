def wordcount(sentence):
    wordcount = {}
    for word in sentence.split():
        wordcount[word] = wordcount.get(word,0)+1
    return wordcount

sentence = "hello there how are you doing today"
print(wordcount(sentence))