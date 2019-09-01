import sys
import re

input_document = sys.argv[1]
output_document = sys.argv[2]

number_of_repeated_word = {}
#Look at the file specified in the console
all_text_in_document = open(input_document)
#Turn all the words lower case so it'll be easier to look at the words
lowercase_words = all_text_in_document.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,50}\b', lowercase_words)

#Loop to find reoccuring words
for word in match_pattern:
    count = number_of_repeated_word.get(word,0)
    number_of_repeated_word[word] = count + 1

#Create a list of all the keys
words_list = number_of_repeated_word.keys()
 
#Outut list to file
for words in sorted(words_list):
    print(words, number_of_repeated_word[words])