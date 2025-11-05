# Write a function that takes an array of words and smashes them together into a sentence 
# and returns the sentence. You can ignore any need to sanitize words or add punctuation, 
# but you should add spaces between each word.
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!

def smash(words):
    sentence = " ".join(words)  # .join() only works for string values
    print(sentence)
    #return sentence

#words  = ["Hello", "my", "name", "is", "Ish"]
words = str([1,2,3,4,5])

smash(words)