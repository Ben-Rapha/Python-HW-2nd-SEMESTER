#KINGSLEY OTTO
#FINAL PROJECT
#SUBTITUTION CYPHER


class Subtitution(): 
    
    def substitutionEncrypt(plainText, key):
        
        alphabet = "abcdefghijklmnopqrstuvwxyz " # alphabet used to help with the subtitution
        plainText = plainText.lower() # lowering all the text so we can have some consistency
        cipherText = ""

        # iterating over the plaintext and replacing the key over the original text
        for ch in plainText:
            idx = alphabet.find(ch)
            cipherText = cipherText + key[idx]
        return cipherText

def main():
    testKey1 = "ouwckbjmpzyexavrltsfgdqihn  " #key which will be used for the encryption. P.S (can be changed by user to meet his/her needs
    f = open("try.txt","r") #opening a file containing a message to be encrypted
    text = f.read() #read every line in the message and store it in variable text
    
    cipherText = Subtitution.substitutionEncrypt(text,testKey1) # call the subtitution encryption class so the message can be encrypted
    
    cipherText = cipherText.replace('k','E') ###############
    cipherText = cipherText.replace('f','T')               #
    cipherText = cipherText.replace('o','A')               #
    cipherText = cipherText.replace('m','H')               #
    #cipherText = cipherText.replace('p','O')              #
    cipherText = cipherText.replace('t','R')               #
    cipherText = cipherText.replace('a','N')               # 
    cipherText = cipherText.replace('s','S')               # 
    cipherText = cipherText.replace('v','O')
    cipherText = cipherText.replace('p','I')              # 
    cipherText = cipherText.replace('j','G')              #    ===========> This are few subtion I made my self in order to help the user to know how the subtution is like
    cipherText = cipherText.replace('b','F')              #
    cipherText = cipherText.replace('x','M')              #                 (you can delete each replaced text if use want to see the origial encryped message)
    cipherText = cipherText.replace('r','P')              #
    cipherText = cipherText.replace('u','B')              #
    cipherText = cipherText.replace('h','Y')              #
    cipherText = cipherText.replace('c','D')
    cipherText = cipherText.replace('e','L')              #
    cipherText = cipherText.replace('d','V')              #
    cipherText = cipherText.replace('q','W')
    cipherText = cipherText.replace('y','K')              #
    cipherText = cipherText.replace('g','U')              #
    cipherText = cipherText.replace('w','C')###############
    
    print(cipherText)
    

main()
