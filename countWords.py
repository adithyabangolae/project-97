string = input("Enter String:")
cCount = 0
wordCount = 1
for i in string:
    cCount = cCount +1
    if (i==' '):
        wordCount = wordCount+1
print("Number of words in the string:")
print(wordCount)
print("Number of characters in the string:")
print(cCount)