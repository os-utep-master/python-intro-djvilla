#################################This program is based on##############################
#    Title: test.py
#    Original Author: Abder-Rahman Ali
#    Date: July 1, 2016
#    Availability: https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965
#
########################################################################################

import sys
import re
import os

#Get terminal arguments
input_document = sys.argv[1]    #File we are reading too
output_document = sys.argv[2]   #File we are writing too

#Create dictionary to hold words
number_of_repeated_word = {}
#Look at the file specified in the console
all_text_in_document = open(input_document)
#Turn all the words lower case so it'll be easier to look at the words
lowercase_words = all_text_in_document.read().lower()

#Grab all the words that are actually words
#i.e. has a non letter before and after to be considered a word
match_pattern = re.findall(r'\b[a-z]{1,50}\b', lowercase_words)

#Loop to find reoccuring words
for word in match_pattern:
    count = number_of_repeated_word.get(word,0)
    number_of_repeated_word[word] = count + 1

#Create a list of all the keys
words_list = number_of_repeated_word.keys()
 
#Open output file
output_file = open(output_document, "w")
#Output sorted list to file
for words in sorted(words_list):
    output_field = words + " "+ str(number_of_repeated_word[words]) + "\n"
    output_file.write(output_field)
    #print(words, number_of_repeated_word[words])

#Close files
all_text_in_document.close()
output_file.close()