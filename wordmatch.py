# word check file 

import re
# this file contains 2 different fuction which helps to guess a words you are trying to
#figure out. Run thi code for the first to get a glimpse on how each fuction works

# This function checks  an uncompleted word in a word list a return a possible  word/words
# which fits in with the uncompleted word
def checkWord(regex):
    resList = []
    wordFile = open('wordlist.txt')
    for line in wordFile:
        if re.match(regex,line[:-1]):
            resList.append(line[:-1])
    return resList
    
print(checkWord('STRAN.EST'))
print(checkWord('a..i.al'))


# this function does the same as the above, but in this case we run an uncompleted word
# against unused alphabet yet. Once a word replacement is found, all found letter must be removed from unsed letters
def checkWord(unused,pattern):
    resList = []
    wordFile = open('wordlist.txt')
    rePat = '['+unused+']'
    regex = re.sub('[a-z]',rePat,pattern) + '$'  
    regex = regex.lower()
    print('matching ', regex)
    for line in wordFile:
        if re.match(regex,line[:-1]):
            resList.append(line[:-1])
    return resList
print(checkWord('bcglnopqvxz' ,'AuOgT') )
    
