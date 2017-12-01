#KINGSLEY OTTO
#SUBTITUTION CYPHER (FINAL PROJECT)

"This program is used to help find letter frequencies in a message or a written piece"
"The user can insert new file namme txt to find letter frequencies"


#this function is used to remove matches into a new one 
def removeMatches(myString,removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr

# this function is used to remove duplicates into a new one       
def removeDupes(myString):
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr

# this function is used to find letter frequency in a message    
def letterFrequency(text):
    text = text.lower()
    nonletters = removeMatches(text,alphabet)
    nonletters = removeDupes(nonletters)
    text = removeMatches(text,nonletters)
    lcount = {}
    total = len(text)
    for ch in text:
        lcount[ch] = lcount.get(ch,0) + 1
    for ch in lcount:
        lcount[ch] = lcount[ch] / total
    return lcount
    
def getFreq(t):
    return t[1]
    
alphabet="abcdefghijklmnopqrstuvwxyz"
f = open("encrpt.txt","r")
text = f.read()
print(text)
lf = letterFrequency(text)
lflist = list(lf.items())
lflist.sort(key=getFreq, reverse=True)
for entry in lflist:
    print("%s %5.3f"%entry)
    
